from l25ExtractTemplate import ReturnInfo_dictlist
from l26RemoveEmphasis import RemoveEmphasis
import re

def RemoveInternalLink(Info_dictlist:list):
    # [[]]を除去 
    # |が[[]]の間にある場合は、|より後ろのみを残す
    # [[ファイル: ]]のパターンは例外なので、そのまま
    Patterns = [re.compile(r'\[\[(?!ファイル:).*?\|(.*?)\]\]'), re.compile(r'\[\[(?!ファイル:)(.*?)\]\]')]
    for pattern in Patterns: 
        #|があるものを先に除く
        journalNum = 0
        for info_dict in Info_dictlist:
            for key, value in info_dict.items():
                # マッチした部分を抜き出した部分で上書き
                Info_dictlist[journalNum][key] = pattern.sub(r'\1', value)
            journalNum += 1

if __name__ == "__main__":
    # 記事ごとに基礎情報の辞書オブジェクトが格納されたリスト
    Info_dictlist = ReturnInfo_dictlist()
    # print(Info_dictlist[3])
    
    RemoveEmphasis(Info_dictlist)
    RemoveInternalLink(Info_dictlist)
    # print(Info_dictlist[3])
    print(Info_dictlist)

