from../3_Normal/l20ReadJson import Read_Json, ExtractJornal_byWord
import re

def OverwriteMatched(Jornals:list, pattern, source:str):
    for i, jornal in enumerate(Jornals):
        for key, value in jornal.items():
            # マッチした部分を上書き
            Jornals[i][key] = pattern.sub(source, value)


def RemoveMarkup(Jornals):
    Patterns = [
        re.compile(r'\'{2,}'), # 'が連続して2回以上続く(強調表現)
        re.compile(r'<!--.*?-->'), #コメントアウト
        re.compile(r'\[\[(?!ファイル:).*?\|(.*?)\]\]'), #内部リンク削除1
        re.compile(r'\[\[(?!ファイル:)(.*?)\]\]'), #内部リンク削除2
        re.compile(r'\[\[ファイル:(.*?)\|*.*?\]\]'), #ファイル名で上書き
        re.compile(r'\{\{(?:lang|Lang)\|.*?\|(.*?)\}\}'), #(lang|言語略名|内容)の内容で上書き
        re.compile(r'\{\{仮リンク\|(.*?)\|*.*?\}\}')    #日本語部分で上書き
    ]
    for i, pattern in enumerate(Patterns):
        if i < 2: #最初の二つのパターンは、削除
            OverwriteMatched(Jornals, pattern, '')
        else:   #他は抜き取った部分で上書き
            OverwriteMatched(Jornals, pattern, r'\1')

if __name__ == "__main__":
    dict_list = Read_Json("/home/ryoma/nock100/3_Normal/jawiki-country.json.gz")
    Jornals = ExtractJornal_byWord(dict_list, 'イギリス')
    RemoveAllMarkup(Jornals)
    print(Jornals[0])

