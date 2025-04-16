from l25ExtractTemplate import ReturnInfo_dictlist
import re

def RemoveEmphasis(Info_dictlist:list):
    pattern = re.compile(r'\'{2,}') # 'が連続して2回以上続く
    journalNum = 0
    for info_dict in Info_dictlist:
        for key, value in info_dict.items():
            Info_dictlist[journalNum][key] = pattern.sub('', value)
        journalNum += 1

if __name__ == "__main__":
    # 記事ごとに基礎情報の辞書オブジェクトが格納されたリスト
    Info_dictlist = ReturnInfo_dictlist()
    print(Info_dictlist[3]['公式国名'])
    
    RemoveEmphasis(Info_dictlist)
    print(Info_dictlist[3]['公式国名'])



