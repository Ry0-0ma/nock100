# 1度に1つのこと しかし、やりすぎない p.140
# 10章無関係の下位問題を抽出する
# コードの欠陥にコメントをつける p.61

from l25ExtractTemplate import ReturnInfo_dictlist
from l26RemoveEmphasis import RemoveEmphasis
from l27RemoveInternalLink import RemoveInternalLink

import re

def OverwriteMatched(Info_dictlist:list, pattern, source:str):
    journalNum = 0
    for info_dict in Info_dictlist:
        for key, value in info_dict.items():
            # マッチした部分を上書き
            Info_dictlist[journalNum][key] = pattern.sub(source, value)
        journalNum += 1

def RemoveAllMarkup(Info_dictlist:list):
    Patterns = [
        re.compile(r'\[\[ファイル:(.*?)\|*.*?\]\]'), #ファイル名で上書き
        re.compile(r'\{\{(?:lang|Lang)\|.*?\|(.*?)\}\}'), #(lang|言語略名|内容)の内容で上書き
        re.compile(r'\{\{仮リンク\|(.*?)\|*.*?\}\}')    #日本語部分で上書き
    ]
    for pattern in Patterns:
        OverwriteMatched(Info_dictlist, pattern, r'\1') #抜き出した部分で上書き
    
    OverwriteMatched(Info_dictlist, re.compile(r'<!--.*?-->'),'') #コメントアウトを消去


if __name__ == "__main__":
    # 記事ごとに基礎情報の辞書オブジェクトが格納されたリスト
    Info_dictlist = ReturnInfo_dictlist()
    
    RemoveEmphasis(Info_dictlist) #FIXME: '''がいくつか残っている
    RemoveInternalLink(Info_dictlist) #FIXME [[]] がいくつか残っている
    # この除去し残っている部分は、近くに固まっている -> その記事を参照できていない？

    RemoveAllMarkup(Info_dictlist) #FIXME: 仮リンク残っている, コメントアウトも1つ残っている
    print(Info_dictlist)


# # [[ファイル: が一つ残った-> 後ろのカッコが}}になっていた
# def RemoveFileTemplate(Info_dictlist:list):
#     #ファイル:の後のファイル名を抜き出す
#     pattern = re.compile(r'\[\[ファイル:(.*?)\|*.*?\]\]')
#     OverwriteMatched(pattern, r'\1')

# # FIXME: コメントアウトが一つ残った
# def DeleteCommentout(Info_dictlist:list):
#     pattern = re.compile(r'<!--.*?-->')
#     OverwriteMatched(pattern, '')

# def RemoveLanguageMarkup(Info_dictlist:list):
#     # {{lang|言語略名|内容}} の内容を抜き出す
#     pattern = re.compile(r'\{\{(?:lang|Lang)\|.*?\|(.*?)\}\}')
#     OverwriteMatched(pattern, r'\1')

# def RemoveInterlanguageLink(Info_dictlist:list):
#     pattern = re.compile(r'\{\{仮リンク\|(.*?)\|*.*?\}\}')
#     OverwriteMatched(pattern, r'\1')