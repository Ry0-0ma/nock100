import json
import gzip

def Read_Json(path:str)->list:
    with gzip.open(path, mode='rt') as file:
        Json_list = file.readlines() #記事ごとに分けて読み込み
        Json_dict = []
        for Jornal in Json_list:
            Json_dict.append(json.loads(Jornal)) #記事ごとに辞書型の要素として格納

        return Json_dict

#word が含まれた記事を抜き出す
def ExtractJornal_byWord(dict_list:list, word:str)->list:
    Jornals = []
    for jornal in dict_list:
        for content in jornal.values(): #タイトルと内容
            if word in content:
                Jornals.append(jornal)
                break #同じ記事を追加しないように
    
    return Jornals

def save_dict(dict_list:list, path:str):
    text = str(dict_list)
    with open(path, mode='w') as file:
        file.write(text)    


if __name__ == "__main__":
    dict_list = Read_Json("/home/ryoma/nock100/3_Normal/jawiki-country.json.gz")


    Jornals = ExtractJornal_byWord(dict_list, 'イギリス')
    # save_dict(Jornals, "/home/ryoma/nock100/3_Normal/JornalEngland.txt")