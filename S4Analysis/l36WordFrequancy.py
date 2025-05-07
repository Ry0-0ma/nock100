# 10章無関係の下位問題を抽出する
# 

import sys
import os
import MeCab
import re

from l30Verb import SplitParsedText

sys.path.append(os.path.abspath("../S3Normal"))
from l20ReadJson import Read_Json, ExtractJournal_byWord




# マッチした部分を上書き
def OverwriteMatched(Journals:list, pattern, source:str):
    for i, journal in enumerate(Journals):
        for key, value in journal.items():
            Journals[i][key] = pattern.sub(source, value)

# 余った記号を削除
def RemoveRemains(Journals:list):
    for i, journal in enumerate(Journals):
        for key, value in journal.items():
            Journals[i][key] = value.replace('{', '').replace('}', '').replace('|', '')\
                .replace('*', '').replace(';', '')

# TODO: 削除できるマークアップを増やす
# www. のリンクが残っている,ファイルも残っている, Category も残っているかも
# <> の間で文字のサイズ指定している部分も残っている
def RemoveMarkup(Journals:list):
    Patterns = [
        re.compile(r'\'{2,}'), # 'が連続して2回以上続く(強調表現)
        re.compile(r'\=''{2,}'), # =が連続して2回以上続く(見出し)
        re.compile(r'\<!--.*?--\>'), #コメントアウト
        re.compile(r'\{\{基礎情報 国\n(.*?)\n\}\}', re.DOTALL), # {{基礎情報 のテンプレート部分を削除
        re.compile(r'\<ref\>.*?\<\/ref\>', re.DOTALL), # <ref>タグで囲まれた部分を削除
        re.compile(r'\<ref.*?\>.*(?:\<\/ref\>)*'),  # <ref タグ内に書かれていても削除, タグどうしで囲まれていないかも(貪欲)
        re.compile(r'\[http.*?\s*(.*?)\]'), # [http://...]のURL部分を削除        
        re.compile(r'\[\[(?!ファイル:).*?\|(.*?)\]\]'), #内部リンク削除1
        re.compile(r'\[\[(?!ファイル:)(.*?)\]\]'), #内部リンク削除2
        re.compile(r'\[\[ファイル:(.*?)\|*.*?\]\]'), #ファイル名で上書き
        re.compile(r'\{\{(?:lang|Lang)\|.*?\|(.*?)\}\}'), #(lang|言語略名|内容)の内容で上書き
        re.compile(r'\{\{仮リンク\|(.*?)\|*.*?\}\}'),    #日本語部分で上書き
        re.compile(r'\{\{.*\|*(.*?)\}\}')     #{{...|...}}の最後の区切り部分で上書き
    ]
    for i, pattern in enumerate(Patterns):
        if i < 6: #最初の6つのパターンは、削除
            OverwriteMatched(Journals, pattern, '')
        else:   #他は抜き取った部分で上書き
            OverwriteMatched(Journals, pattern, r'\1')
    RemoveRemains(Journals) #残った記号を削除


def CountAppearance(Words:list, wordfrequancy:dict):
    # POS: Part Of Speech 品詞
    ExcludePOS = ['記号', '助詞', '副詞', '助動詞']
    appearance = 0
    for word in Words:
        if word['features'][0] in ExcludePOS:
            continue
        surface = word['surface']
        if surface in wordfrequancy.keys():
            wordfrequancy[surface] += 1
        else:
            wordfrequancy[surface] = 1
        appearance += 1
    
    return appearance

    
def SortFrequancy(Journals:list)->dict:
    tagger = MeCab.Tagger('--rcfile=/etc/mecabrc -d /var/lib/mecab/dic/debian')
    wordfrequancy = {}
    total_appearance = 0
    for journal in Journals:
        # list->dict(surface, features)
        Words = SplitParsedText(tagger.parse(journal['text']))
        total_appearance += CountAppearance(Words, wordfrequancy)
    # 各頻度を appearance で割る
    wordfrequancy = {key: value/total_appearance for key, value in wordfrequancy.items()} #上書き
    wordfrequancy = dict(sorted(wordfrequancy.items(), key=lambda x:x[1], reverse=True))
    return wordfrequancy

def PrintFrequantWords(wordfrequancy:dict, TopNum:int):
    idx = 0
    for key, value in wordfrequancy.items():
        print(key,'\t', '頻度:', value)
        idx += 1
        if idx >= TopNum:
            break

if __name__ == "__main__":
    Journals = Read_Json("/home/ryoma/nock100/S3Normal/jawiki-country.json.gz")
    # Journals = ExtractJournal_byWord(dict_list, 'イギリス')
    RemoveMarkup(Journals)
    wordfrequancy = SortFrequancy(Journals)
    PrintFrequantWords(wordfrequancy, 20)


"""
し       頻度: 0.020043890472145935
年       頻度: 0.017621938337766933
.        頻度: 0.012048322633773244
いる     頻度: 0.01166999366218133
れ       頻度: 0.011302443293768673
-        頻度: 0.011023277471425922
さ       頻度: 0.010269853109195873
する     頻度: 0.007769217171608297
=        頻度: 0.007580591615971303
月       頻度: 0.007412445406374897
人       頻度: 0.007286335749177593
日       頻度: 0.005543435615091769
:        頻度: 0.005279359837199978
国       頻度: 0.005217921799078214
1        頻度: 0.005154328040320599
/        頻度: 0.004367490008234853
的       頻度: 0.004175630871644082
2        頻度: 0.004018263265226933
語       頻度: 0.003993472477914642
なっ     頻度: 0.003913710814388142
"""


