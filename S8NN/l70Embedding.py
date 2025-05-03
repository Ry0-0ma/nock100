# 自分の考えをコメント
from gensim.models import KeyedVectors
import numpy as np

def EmbeddingMX(model)->(np.ndarray, dict, dict):
    # 語彙数と単語ベクトル次元数を取得
    vocab_num = len(model.key_to_index)
    wordvec_dim = model.vector_size

    # 先頭はパディング用に0ベクトルを入れる
    embMX = np.zeros((vocab_num+1, wordvec_dim), dtype=np.float32)
    # 各行のインデックス番号（トークンID）と、単語（トークン）への双方向の対応付け
    word2idx = {"<pad>": 0} #先頭はパディング
    idx2word = {0: "<pad>"}

    # 単語ベクトルを埋め込む
    for i, word in enumerate(model.key_to_index):
        # 先頭はパディング行なので、i+1から始める
        embMX[i+1] = model[word]
        word2idx[word] = i+1
        idx2word[i+1] = word

    return embMX, word2idx, idx2word

def PrintEmbeddingMX(embMX:np.ndarray, word2idx:dict, idx2word:dict, topN:int=5):
    print(f"Embedding matrix shape: {embMX.shape}")
    # 双方向の対応付けができているかの確認
    for i in range(topN):
        print(f"Word ID: {i}, Word: {idx2word[i]}, CheckID: {word2idx[idx2word[i]]}")
    # 埋め込みベクトルの確認
    for i in range(topN):
        print(f"Word ID: {i}, Vector: {embMX[i]}")

if __name__=='__main__':
    # git上にはこのモデルない
    model = KeyedVectors.load('../S6WordVector/GoogleNews_WordVec.kv')

    embMX, word2idx, idx2word = EmbeddingMX(model)
    PrintEmbeddingMX(embMX, word2idx, idx2word)

"""
Embedding matrix shape: (3000001, 300)
Word ID: 0, Word: <pad>, CheckID: 0
Word ID: 1, Word: </s>, CheckID: 1
Word ID: 2, Word: in, CheckID: 2
Word ID: 3, Word: for, CheckID: 3
Word ID: 4, Word: that, CheckID: 4
"""