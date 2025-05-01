import pandas as pd
from collections import Counter
            

def FeatureVector(dataframe):
    dict_list = []
    for line in dataframe.itertuples():
        # 空白のみの要素を削除しながら追加
        words = [word.strip() for word in line.sentence.split(' ') if word.strip()]
        Feature = dict(Counter(words))
        dict_list.append({'text': line.sentence, 'label':line.label, 'feature':Feature})
    return dict_list

if __name__ == "__main__":
    Train = pd.read_csv('SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = FeatureVector(Train)
    print(Train_dict)

    Develop = pd.read_csv('SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = FeatureVector(Develop)
    print(Dev_dict)

"""
[{'text': 'hide new secretions from the parental units ', 'label': 0, 'feature': {'hide': 1, 'new': 1, 'secretions': 1, 'from': 1, 'the': 1, 'parental': 1, 'units': 1}}, 
"""