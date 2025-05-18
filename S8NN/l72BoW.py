import pandas as pd
import torch
import torch.nn as nn

from gensim.models import KeyedVectors
from l71Text2TokenID import Text2TokenID

class LogRegClassifier(nn.Module):
    def __init__(self, embVec_size):
        super().__init__()
        # 入力と重みベクトルとの内積を計算
        self.linear = nn.Linear(embVec_size, 1)
        # self.sigmoid = nn.Sigmoid()

    def forward(self, mean_embVec)->torch.tensor:
        return self.linear(mean_embVec)
        # 損失関数 は nn.BCEWithLogitsLoss を使用する
        #  self.sigmoid(self.linear(mean_embVec))ならnn.BCELoss()
        

# l71のと違い: 中身をtensor にした
def EmbeddingMX(model)->(torch.tensor, dict, dict):
    # 語彙数と単語ベクトル次元数を取得
    vocab_num = len(model.key_to_index)
    wordvec_dim = model.vector_size

    # 先頭はパディング用に0ベクトルを入れる
    embMX = torch.zeros((vocab_num+1, wordvec_dim), dtype=torch.float32)
    # 各行のインデックス番号（トークンID）と、単語（トークン）への双方向の対応付け
    word2idx = {"<pad>": 0} #先頭はパディング
    idx2word = {0: "<pad>"}

    # 単語ベクトルを埋め込む
    for i, word in enumerate(model.key_to_index):
        # 先頭はパディング行なので、i+1から始める
        embMX[i+1] = torch.from_numpy(model[word].copy()) #model は書き込み不可なので、copy()する
        word2idx[word] = i+1
        idx2word[i+1] = word

    return embMX, word2idx, idx2word

    # text が含まれるdict_listでの添え字を返す
def IdxText_dictlist(text:str, dict_list:list):
    for idx, dictionary in enumerate(dict_list):
        if dictionary.get('text') == text: #get関数はキーが存在しなくてもエラーを防ぐ
            return idx
    return None

def Emb2MeanVec(text:str, dict_list:list, embMX:torch.tensor):
    idx = IdxText_dictlist(text, dict_list)
    if not idx: #入力textはlistにない
        return None
    
    # 単語ベクトルの平均ベクトル
    MeanVec = torch.zeros(embMX.shape[1], dtype=embMX.dtype)
    
    WordVec_IDs = dict_list[idx]['input_ids']
    for ID in WordVec_IDs:
        MeanVec += embMX[ID]/len(WordVec_IDs)
    return MeanVec    

if __name__=='__main__':
    model = KeyedVectors.load('../S6WordVector/GoogleNews_WordVec.kv')
    embMX, word2idx, _ = EmbeddingMX(model)

    Train = pd.read_csv('../S7ML/SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = Text2TokenID(Train, word2idx)

    LogReg = LogRegClassifier(embMX.shape[1])


    