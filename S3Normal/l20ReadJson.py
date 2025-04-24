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
    dict_list = Read_Json("/home/ryoma/nock100/S3Normal/jawiki-country.json.gz")

    Journals = ExtractJournal_byWord(dict_list, 'イギリス')
    save_dict(Journals, "/home/ryoma/nock100/S3Normal/JournalEngland.txt")