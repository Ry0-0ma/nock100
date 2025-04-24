from l20ReadJson import Read_Json, save_dict
import numpy as np

def DivideLine(dict_list:list)->list:
    Jornal_line = []
    for jornal in dict_list:
        Jornal_line.append(str(jornal).split('\\n')) #改行文字ごとに分割したリストを格納
    
    return Jornal_line  #[記事->行ごと] list->list->str

def Findword(line:str, words:list)->bool:
    for word in words:
        if word in line:
            return True
    return False

def ExtractLines(Jornal_line:list, words:list)->list:
    extracted = []
    for jornal in Jornal_line:
        for line in jornal:
            if Findword(line,words):
                extracted.append(line)

    return extracted            

if __name__ == "__main__":
    dict_list = Read_Json("/home/ryoma/nock100/3_Normal/jawiki-country.json.gz")

    Jornal_line = DivideLine(dict_list)
    words = ['Category:', 'カテゴリ:']
    extracted = ExtractLines(Jornal_line, words)

    save_dict('\n'.join(extracted), "/home/ryoma/nock100/3_Normal/CategoryLine.txt")


