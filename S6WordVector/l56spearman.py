from gensim.models import KeyedVectors
from scipy.stats import spearmanr
import pandas as pd
import numpy as np

def WordVec_Similarity(model, Word1:list, Word2:list):
    WordVec_sim = np.zeros(len(Word1))
    for word1, word2, i in zip(Word1, Word2, range(len(Word1))):
        WordVec_sim[i] = model.similarity(word1, word2)
    return WordVec_sim

if __name__ == "__main__":
    Analogy = pd.read_csv("wordsim353/combined.csv", encoding="utf-8")
    # print(Analogy.index) #RangeIndex(start=0, stop=353, step=1)
    # print(Analogy.columns) #Index(['Word 1', 'Word 2', 'Human (mean)'], dtype='object')
    Word1 = Analogy["Word 1"]
    Word2 = Analogy["Word 2"]
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    WordVec_sim = WordVec_Similarity(model, Word1, Word2)

    # 単語ベクトルの類似度と人間の類似度判定のスピアマン相関係数
    Human_sim = np.array(Analogy["Human (mean)"])
    Spearman = spearmanr(Human_sim, WordVec_sim)
    print(f"Spearmanの順位相関係数: {Spearman.correlation:.5f}")

    """
    Spearmanの順位相関係数: 0.70002
    """