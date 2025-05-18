# 汎用コードをつくる

import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors

from l71Text2TokenID import Text2TokenID
from l72BoW import EmbeddingMX, LogRegClassifier, Emb2MeanVec


def Train_LogReg(Train_dict:list, embMX:torch.tensor, epochs:int=10, learning_rate:float=0.001):
    # モデルの初期化
    model = LogRegClassifier(embMX.shape[1]) 
    optimizer = torch.optim.Adam(model.parameters(), lr=0.001) #loss を最小化するためにパラメータを更新
    # 損失関数のインスタンス化
    loss_criterion = nn.BCEWithLogitsLoss() #入力はsigmoidの出力ではない: この中でsigmoidが適用される

    # 学習
    print_epoch = epochs // 10 #学習中10回表示
    loss_list = []
    for epoch in range(epochs):
        model.train()
        for dict_batch in Train_dict: #キー: text, label, input_ids
            optimizer.zero_grad() #勾配を初期化
            MeanVec = Emb2MeanVec(dict_batch['text'], Train_dict, embMX)
            if MeanVec is None: #入力textはlistにない
                continue

            # シグモイド関数を適用する前のモデルの出力値
            logit = model(MeanVec) #平均ベクトルと重みベクトルの内積
            loss = loss_criterion(logit, dict_batch['label'])
            loss.backward() # model.parameters() の.gradに勾配が格納される
            optimizer.step() # 勾配を用いてパラメータを更新
        if (epoch+1) % print_epoch == 0:
            print(f'Epoch {epoch+1}/{epochs}, Loss: {loss.item()}')
            loss_list.append(loss.item())
    
    return model, loss_list

def Plot_Loss(loss_list:list, output_file:str='loss.png'):
    plt.figure()
    plt.plot(loss_list)
    plt.title('LogRegClassifier: Loss')
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.savefig(output_file)
    plt.close()

if __name__=='__main__':
    WordVec_model = KeyedVectors.load('../S6WordVector/GoogleNews_WordVec.kv')
    embMX, word2idx, idx2word = EmbeddingMX(WordVec_model)

    Train = pd.read_csv('../S7ML/SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = Text2TokenID(Train, word2idx)

    _, loss_list= Train_LogReg(Train_dict, embMX)
    Plot_Loss(loss_list)

"""
Epoch 1/10, Loss: 0.4832812249660492
Epoch 2/10, Loss: 0.4858943521976471
Epoch 3/10, Loss: 0.4888724386692047
Epoch 4/10, Loss: 0.4906018376350403
Epoch 5/10, Loss: 0.4913333058357239
Epoch 6/10, Loss: 0.49136263132095337
Epoch 7/10, Loss: 0.4909258484840393
Epoch 8/10, Loss: 0.4901946187019348
Epoch 9/10, Loss: 0.4892962574958801
Epoch 10/10, Loss: 0.48832428455352783
"""


"""
改善のためのチェックリスト

学習率を調整する（0.001 → 0.0001 や 0.01）。
入力データ（単語ベクトルの平均）を正規化する。
モデルの重み初期化を見直す。
損失関数とラベルの設定を確認する。
クラスの不均衡がある場合は重み付き損失関数を使用する。
エポック数を増やしてみる。
データの前処理やラベルの質を確認する。
"""
