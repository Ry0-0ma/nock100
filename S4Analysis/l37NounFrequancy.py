import sys
import os
import MeCab


from l30Verb import SplitParsedText
from l36WordFrequancy import RemoveMarkup, PrintFrequantWords

sys.path.append(os.path.abspath("../S3Normal"))
from l20ReadJson import Read_Json, ExtractJournal_byWord

def CountNounAppearance(Words:list, nounfrequancy:dict):
    apparance = 0
    for word in Words:
        if word['features'][0] != '名詞':
            continue
        surface = word['surface']
        if surface in nounfrequancy.keys():
            nounfrequancy[surface] += 1
        else:
            nounfrequancy[surface] = 1
        apparance += 1
    return apparance
    
def SortNounFrequancy(Journals:list)->dict:
    tagger = MeCab.Tagger('--rcfile=/etc/mecabrc -d /var/lib/mecab/dic/debian')
    nounfrequancy = {}
    total_appearance = 0
    for journal in Journals:
        # list->dict(surface, features)
        Words = SplitParsedText(tagger.parse(journal['text']))
        total_appearance += CountNounAppearance(Words, nounfrequancy)
    # 各頻度を appearance で割る
    nounfrequancy = {key: value/total_appearance for key, value in nounfrequancy.items()} #上書き
    nounfrequancy = dict(sorted(nounfrequancy.items(), key=lambda x:x[1], reverse=True))
    return nounfrequancy

if __name__ == "__main__":
    Journals = Read_Json("/home/ryoma/nock100/S3Normal/jawiki-country.json.gz")
    # Journals = ExtractJournal_byWord(dict_list, 'イギリス')
    RemoveMarkup(Journals)
    # print(Journals[0]['text'])
    nounfrequancy = SortNounFrequancy(Journals)
    PrintFrequantWords(nounfrequancy, 20)

    """
年       頻度: 0.02093575084548471
.        頻度: 0.014314014493291826
-        頻度: 0.013096209180792226
=        頻度: 0.009006124882029112
月       頻度: 0.008806358710893532
人       頻度: 0.008656534082541845
日       頻度: 0.0065858808855788036
:        頻度: 0.0062721455527056155
国       頻度: 0.006199154067098383
1        頻度: 0.006123601476733003
/        頻度: 0.00518879824000881
的       頻度: 0.004960859916533596
2        頻度: 0.004773899269188757
語       頻度: 0.00474444656447005
こと     頻度: 0.004621513536078923
,        頻度: 0.00420661456525887
3        頻度: 0.004078559327351446
="       頻度: 0.0036803075374593586
日本     頻度: 0.003499749652009891
政府     頻度: 0.00349334689011452
    """