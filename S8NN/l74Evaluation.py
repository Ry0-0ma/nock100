# 無関係の下位問題を抽出する
import pandas as pd
import torch
import torch.nn as nn
import matplotlib.pyplot as plt
from gensim.models import KeyedVectors
from sklearn.metrics import accuracy_score

from l71Text2TokenID import Text2TokenID
from l72BoW import EmbeddingMX, LogRegClassifier, Emb2MeanVec
from l73Train import Train_LogReg, Plot_Loss

def TrueLabels(dict_list:list):
    labels = torch.zeros(len(dict_list), dtype=torch.float)
    for i, dictionary in enumerate(dict_list):
        labels[i] = dictionary['label']
    return labels

def Evaluate_LogReg(Dev_dict:list, model:LogRegClassifier, embMX:torch.tensor):
    true_labels = TrueLabels(Dev_dict)
    model.eval() #評価モードに切り替え
    pred_labels = torch.zeros(len(Dev_dict), dtype=torch.float)
    with torch.no_grad():
        for i, dictionary in enumerate(Dev_dict):
            MeanVec = Emb2MeanVec(dictionary['text'], Dev_dict, embMX)
            if MeanVec is None:
                continue
            output = model(MeanVec)
            # 一時的にシグモイド関数を適用したい場合
            pred_labels[i] = torch.sigmoid(output).item().round() # 0.5以上なら1, それ以外は0
            # nn.Sigmoid はモデルの一部として定義する場合に使う
            
    return accuracy_score(true_labels, pred_labels)
      

if __name__=='__main__':
    WordVec_model = KeyedVectors.load('../S6WordVector/GoogleNews_WordVec.kv')
    embMX, word2idx, idx2word = EmbeddingMX(WordVec_model)

    Train = pd.read_csv('../S7ML/SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = Text2TokenID(Train, word2idx)

    # 学習
    model, loss_list= Train_LogReg(Train_dict, embMX)
    Plot_Loss(loss_list)

    # 評価
    Develop = pd.read_csv('../S7ML/SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = Text2TokenID(Develop, word2idx)
    accuracy = Evaluate_LogReg(Dev_dict, model, embMX)
    print(f'Accuracy: {accuracy:.4f}')