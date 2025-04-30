import re

def ExtractCategoryName(categorylines:list)->list:
    categories = []
    for line in categorylines:
        # stopwords: |, ], }
        #(Category: または カテゴリ: )の後から stopwords までの単語を抜き出す
        patern = r'(?:Category:|カテゴリ:)([^|\]\}]+)'
        categories.append(str(re.findall(patern, line)))

    return categories

def SaveList(List:list, path:str):
    chars = "\n".join(List)
    with open(path, mode='w') as file:
        file.write(chars)


if __name__ == "__main__":
    with open("CategoryLine.txt") as file:
        categorylines = file.readlines()
    
    categories = ExtractCategoryName(categorylines)

    SaveList(categories, "CategoryNames.txt")

"""
['エジプト']
['共和国']
['軍事政権']
['フランコフォニー加盟国']
['オーストリアの食文化']
['オーストリアの作曲家']
['オーストリア']
['内陸国']
['欧州連合加盟国']
['共和国']
['連邦制国家']
"""


'''
( ) にマッチする部分を抽出する (キャプチャグループ)
(?: ) は抽出はしないが、グループ化はする
[] この中に書かれた文字のどれか1文字がマッチ (文字クラス)
[^ ] 文字クラスの先頭に ^ がつくとそれ以外の文字とマッチ (否定)
+ 直前のパターンが1回以上繰り返される

'''