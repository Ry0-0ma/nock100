import pandas as pd

def IncludeVocabraly(words:list, word2idx:list):
    for word in words:
        if word in word2idx.keys():
            return True
    return False #全単語語彙に含まれていない

def Text2TokenID(dataframe, word2idx:list):
    dict_list = []
    for line in dataframe.itertuples():
        # 空白のみの要素を削除しながら追加
        words = [word.strip() for word in line.sentence.split(' ') if word.strip()]
        if not IncludeVocabraly(words):
            continue
            
            

if __name__=="__main__":
    Train = pd.read_csv('../S7ML/SST-2/train.tsv', sep='\t', encoding='utf-8')

    