import pandas as pd
import torch

from gensim.models import KeyedVectors
from l70Embedding import EmbeddingMX

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
        if not IncludeVocabraly(words, word2idx):
            continue
        tokenID = torch.tensor([word2idx[word] for word in words if word in word2idx])
        dict_list.append({'text':line.sentence,
                        'label':torch.tensor([line.label], dtype=torch.float),
                        'input_ids': tokenID
                        })
    return dict_list
            

if __name__=="__main__":
    model = KeyedVectors.load('../S6WordVector/GoogleNews_WordVec.kv')
    embMX, word2idx, idx2word = EmbeddingMX(model)
    
    Train = pd.read_csv('../S7ML/SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = Text2TokenID(Train, word2idx)

    Develop = pd.read_csv('../S7ML/SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = Text2TokenID(Develop, word2idx)

    print('Train')
    print(Train_dict[:5])
    print('Develop')
    print(Dev_dict[:5])

"""
Train
[{'text': 'hide new secretions from the parental units ', 'label': tensor([0.]), 'input_ids': tensor([  5785,     66, 113845,     18,     12,  15095,   1594])}, {'text': 'contains no wit , only labored gags ', 'label': tensor([0.]), 'input_ids': tensor([ 3475,    87, 15888,    90, 27695, 42637])}, {'text': 'that loves its characters and communicates something rather beautiful about human nature ', 'label': tensor([1.]), 'input_ids': tensor([    4,  5053,    45,  3305, 31647,   348,   904,  2815,    47,  1276,
         1964])}, {'text': 'remains utterly satisfied to remain the same throughout ', 'label': tensor([0.]), 'input_ids': tensor([  987, 14528,  4941,   873,    12,   208,   898])}, {'text': 'on the worst revenge-of-the-nerds clichés the filmmakers could dredge up ', 'label': tensor([0.]), 'input_ids': tensor([    6,    12,  1445, 43789,    12, 10946,    76, 41349,    42])}]
Develop
[{'text': "it 's a charming and often affecting journey . ", 'label': tensor([1.]), 'input_ids': tensor([   16, 13259,   640,  5199,  3900])}, {'text': 'unflinchingly bleak and desperate ', 'label': tensor([0.]), 'input_ids': tensor([136642,  12607,   4984])}, {'text': 'allows us to hope that nolan is poised to embark a major career as a commercial yet inventive filmmaker . ', 'label': tensor([1.]), 'input_ids': tensor([  1488,    165,    684,      4, 953829,      5,   6091,  14671,    339,
           513,     15,   1073,    507,  24346,  11212])}, {'text': "the acting , costumes , music , cinematography and sound are all astounding given the production 's austere locales . ", 'label': tensor([1.]), 'input_ids': tensor([   12,  2527, 10358,   637, 37102,  1868,    20,    53, 18600,   483,
           12,   621, 37066, 30723])}, {'text': "it 's slow -- very , very slow . ", 'label': tensor([0.]), 'input_ids': tensor([  16, 1804,  139,  139, 1804])}]
"""