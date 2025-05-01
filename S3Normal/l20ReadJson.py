# 1度に一つのこと
# ライブラリに親しむ

import json
import gzip

def Read_Json(path:str)->list:
    with gzip.open(path, mode='rt') as file:
        Json_list = file.readlines()
        Json_dict = []
        for Journal in Json_list:
            Json_dict.append(json.loads(Journal))

        return Json_dict

#word が含まれた記事を抜き出す
def ExtractJournal_byWord(dict_list:list, word:str)->list:
    Journals = []
    for Journal in dict_list:
        for content in Journal.values(): #タイトルと内容
            if word in content:
                Journals.append(Journal)
                break #同じ記事を追加しないように
    
    return Journals

def save_dict(dict_list:list, path:str):
    text = str(dict_list)
    with open(path, mode='w') as file:
        file.write(text)    

if __name__ == "__main__":
    #list - dict - key(title, text)
    dict_list = Read_Json("jawiki-country.json.gz")

    Journals = ExtractJournal_byWord(dict_list, 'イギリス')
    save_dict(Journals, "JournalEngland.txt")

"""
[{'title': 'エジプト', 'text': '{{otheruses|主に現代のエジプト・アラブ共和国|古代|古代エジプト}}\n
{{基礎情報 国\n
|略名 =エジプト\n
|漢字書き=埃及\n
|日本語国名 =エジプト・アラブ共和国\n
|公式国名 ={{lang|ar|\'\'\'جمهورية مصر العربية\'\'\'}}\n
|国旗画像 =Flag of Egypt.svg\n|国章画像 =[[ファイル:Coat_of_arms_of_Egypt.svg|100px|エジプトの国章]]\n|国章リンク =（[[エジプトの国章|国章]]）\n
|標語 =なし\n|位置画像 =
"""