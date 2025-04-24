# p.61コードの欠陥にコメント
# 10章無関係の下位問題を抽出する

import sys
import os
import math

from l30Verb import SplitParsedText
from l36WordFrequancy import RemoveMarkup
from l37NounFrequancy import SortNounFrequancy

sys.path.append(os.path.abspath("../S3Normal"))
from l20ReadJson import Read_Json, ExtractJournal_byWord

def CountDocumentAppearance(Journals:list, DF:dict, noun:str):
    for journal in Journals:
        if noun in journal['text']:
            if noun in DF.keys():
                DF[noun] += 1
            else:
                DF[noun] = 1

def CountIDF(Journals:list, nounfrequancy:dict):
    DF = {} # Document Frequency
    for noun in nounfrequancy.keys():
        CountDocumentAppearance(Journals, DF, noun)
    # IDF(noun) = log(総文書数/nounの出現文書数)
    IDF = {key: math.log(len(Journals)/value) for key,value in DF.items()}
    return IDF

def  SortTF_IDF(TF:dict, IDF:dict)->dict:
    TF_IDF = {}
    for noun in TF.keys():
        if noun in IDF.keys():
            TF_IDF[noun] = TF[noun] * IDF[noun]
    TF_IDF = dict(sorted(TF_IDF.items(), key=lambda x:x[1], reverse=True))
    return TF_IDF

def PrintTF_IDF(TF_IDF:dict, TF:dict, IDF:dict, TopNum:int):
    for i, noun in enumerate(TF_IDF.keys()):
        if i >= TopNum:
            break
        print(f"{noun}, \t, TF: {TF[noun]}, IDF: {IDF[noun]}, TF-IDF: {TF_IDF[noun]}")


if __name__ == "__main__":
    dict_list = Read_Json("/home/ryoma/nock100/S3Normal/jawiki-country.json.gz")
    Journals = ExtractJournal_byWord(dict_list, '日本') #FIXME: 日本の記事のみを抽出できてなそう
    RemoveMarkup(Journals) #FIXME: マークアップ削除も足りてなさそう
    TF = SortNounFrequancy(Journals)
    IDF = CountIDF(Journals, TF)
    TF_IDF = SortTF_IDF(TF, IDF)
    PrintTF_IDF(TF_IDF, TF, IDF, 20)

    """
    align,  , TF: 0.0023668808626544757, IDF: 0.9721711902686117, TF-IDF: 0.0023010133854708
    香港,   , TF: 0.0006760655848748888, IDF: 2.493640329756755, TF-IDF: 0.001685864408004611
    ロシア,         , TF: 0.001335196964348287, IDF: 1.1476198677748044, TF-IDF: 0.0015322985636787015
    韓国,   , TF: 0.0008024208097937023, IDF: 1.8271613962789708, TF-IDF: 0.0014661523272259636
    ポーランド,     , TF: 0.0006695524289512386, IDF: 2.1422424429188665, TF-IDF: 0.0014343436310587621
    県,     , TF: 0.002002144130930066, IDF: 0.6177977433181585, TF-IDF: 0.0012369201258862904
    />(,    , TF: 0.0003425920015839995, IDF: 3.492169159867882, TF-IDF: 0.0011963892223490517
    ウクライナ,     , TF: 0.0005236577362614746, IDF: 2.26002547857525, TF-IDF: 0.001183479826003971
    北朝鮮,         , TF: 0.000539289310478235, IDF: 2.1422424429188665, TF-IDF: 0.0011552884499189252
    high,   , TF: 0.0004220525038525317, IDF: 2.7300291078209855, TF-IDF: 0.0011522156205461401
    style,  , TF: 0.001697328433703237, IDF: 0.6340582641899388, TF-IDF: 0.0010762051204341021
    text,   , TF: 0.0007411971441113905, IDF: 1.4307461236907244, TF-IDF: 0.0010604649408280072
    大統領,         , TF: 0.0032461569123472503, IDF: 0.32008549650644025, TF-IDF: 0.0010390477470264827
    center,         , TF: 0.0009587365519613066, IDF: 1.0813704822336037, TF-IDF: 0.0010367494075293805
    アルゼンチン,   , TF: 0.00044549986517767237, IDF: 2.302585092994046, TF-IDF: 0.0010258013484889656
    ネパール,       , TF: 0.00027615781116276767, IDF: 3.6463198396951406, TF-IDF: 0.001006959705729584
    :#,     , TF: 0.0006083287632689269, IDF: 1.6538896750049343, TF-IDF: 0.0010061086605789992
    div,    , TF: 0.0003986051425273911, IDF: 2.493640329756755, TF-IDF: 0.000993977859054742
    low,    , TF: 0.00042335513503726174, IDF: 2.3470368555648795, TF-IDF: 0.0009936301049250998
    スペイン,       , TF: 0.0010889996704343103, IDF: 0.9054798157699394, TF-IDF: 0.000986067220958384
    """