#無関係の下位問題を抽出する 
# 自分の考えをコメント

import pandas as pd
import torch
import torch.nn as nn
from gensim.models import KeyedVectors
from sklearn.metrics import accuracy_score

from l71Text2TokenID import Text2TokenID

def MaxToken(dict_list:list)->(int, dict):
    #トークン数でソートするために、元の配列の添え字をキーにして辞書を作成
    TokenLength = {}
    for i, dictionary in enumerate(dict_list):
        max_token = max(max_token, len(dictionary['input_ids']))
        TokenLength[i] = len(dictionary['input_ids'])
    return max_token, TokenLength

def collate(dict_list:list):
    # 最大トークン数 と トークン数の辞書を取得
    max_token, TokenLength = MaxToken(dict_list)
    SortedToken = sorted(TokenLength.items(), key=lambda x: x[1], reverse=True) #トークン数でソート
    
    padding_IDs = torch.zeros(max_token, len(dict_list), dtype=torch.dict_list[0]['input_ids'].dtype)
    padding_label = torch.zeros(max_token, dtype=torch.float)
    for i, dictionary in enumerate(dict_list):
        # トークン数が最大トークン数より小さい場合、0でパディングする
        if TokenLength[i] < max_token:
            padding = torch.zeros(max_token - TokenLength[i], dtype=dict)
            dict_list[i]['input_ids'] = torch.cat([dictionary['input_ids'], padding])
        else:
            dict_list[i]['input_ids'] = dictionary['input_ids']


if __name__=='__main__':
    WordVec_model = KeyedVectors.load('../S6WordVector/GoogleNews_WordVec.kv')
    _, word2idx, _ = EmbeddingMX(WordVec_model)

    Train = pd.read_csv('../S7ML/SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = Text2TokenID(Train, word2idx)


    