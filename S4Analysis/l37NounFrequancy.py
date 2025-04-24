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
    dict_list = Read_Json("/home/ryoma/nock100/S3Normal/jawiki-country.json.gz")
    Journals = ExtractJournal_byWord(dict_list, 'イギリス')
    RemoveMarkup(Journals)
    # print(Journals[0]['text'])
    nounfrequancy = SortNounFrequancy(Journals)
    PrintFrequantWords(nounfrequancy, 20)

    """
    年       頻度: 0.02097227433174325
    .        頻度: 0.014231131461474261
    -        頻度: 0.012770193183819419
    =        頻度: 0.008759504138559429
    月       頻度: 0.00859564628142204
    人       頻度: 0.008566550026416337
    :        頻度: 0.006323075627292288
    日       頻度: 0.006244975153329607
    1        頻度: 0.006166874679366927
    国       頻度: 0.005823845146668096
    /        頻度: 0.005119409499161568
    的       頻度: 0.005113283971791946
    2        頻度: 0.004848354913055796
    こと     頻度: 0.004716656074608924
    語       頻度: 0.004666120473809542
    ,        頻度: 0.0041806724297670005
    3        頻度: 0.004120948537913186
    ="       頻度: 0.003802421114692843
    日本     頻度: 0.0036018100933377234
    政府     頻度: 0.0034777681641028784
    """