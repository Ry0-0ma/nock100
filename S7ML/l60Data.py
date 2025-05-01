# ライブラリに親しむ
import pandas as pd
import numpy as np
from collections import Counter

def Print_CountLabel(labels):
    count = Counter(labels)
    print(count)
    print(f'positive: {count[1]} negative: {count[0]}')

if __name__ == "__main__":
    Train = pd.read_csv('SST-2/train.tsv', sep='\t', encoding='utf-8')
    # print(Train.columns)  #Index(['sentence', 'label'], dtype='object')
    print('train.tsv')
    Print_CountLabel(Train['label'])

    Develop = pd.read_csv('SST-2/dev.tsv', sep='\t', encoding='utf-8')
    print('dev.tsv')
    Print_CountLabel(Develop['label'])

"""
train.tsv
Counter({1: 37569, 0: 29780})
positive: 37569 negative: 29780
dev.tsv
Counter({1: 444, 0: 428})
positive: 444 negative: 428
"""