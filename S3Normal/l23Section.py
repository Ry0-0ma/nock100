#11章 1度に1つのタスク
# ライブラリに親しむ

from l20ReadJson import Read_Json
import re

def Extractpattern(dict_list:list, pattern:str)->list:
    Matched = []
    for jornal in dict_list:
        Matched += re.findall(pattern, jornal['text'])

    return Matched

def ExtractTitle(Matched:list)->list:
    Titles = []
    for match in Matched: #match: (連続した=, セクション名)
        Titles.append(match[1])
    
    return Titles

def CountLevel(Matched:list)->list:
    Levels = []
    for match in Matched:
        # len(match[0]): 連続した=の数
        Levels.append(len(match[0])-1) #=の数 -1 がレベル
    
    return Levels

def MergeTitleAndLevel(Titles:list, Levels:list)->str:
    Sections = []
    for i in range(len(Titles)):
        # セクション名(レベル) の形式で記述
        section = Titles[i]+' ('+str(Levels[i])+")"
        Sections.append(section)
    
    return "\n".join(Sections)


if __name__ == "__main__":
    #list - dict - key(title, text)
    dict_list = Read_Json("jawiki-country.json.gz")
    
    # 連続した= と =に囲まれた セクション名を抽出
    pattern = r'(={2,})\s*(.*?)\s*\1'
    Matched = Extractpattern(dict_list, pattern)
    
    # print(Matched[0])
    Titles = ExtractTitle(Matched)
    Levels = CountLevel(Matched)
    Sections = MergeTitleAndLevel(Titles, Levels)

    with open("Sections.txt", mode='w') as file:
        file.write(Sections)

"""
国号 (1)
歴史 (1)
古代エジプト (2)
アケメネス朝ペルシア (2)
ヘレニズム文化 (2)
ローマ帝国 (2)
イスラム王朝 (2)
オスマン帝国 (2)
"""


"""
{m,n} m回からn回繰り返す-> ={2,}で=2個以上連続したもの
\\s 空白文字
* 0回以上の繰り返し: 無くてもよい
. 任意の1文字
(.*?) :マッチングする最短の文字列をキャプチャ
\\1 :1番目にキャプチャした文字列と同じ文字列 -> =の繰り返し

"""