from l20ReadJson import Read_Json
from l23Section import Extractpattern

import re


if __name__ == "__main__":
    #list - dict - key(title, text)
    dict_list = Read_Json("/home/ryoma/nock100/3_Normal/jawiki-country.json.gz")

    # ファイル:, file:, File: どれかの後から 
    # |, ], } のどれか までの間を抽出
    Files = Extractpattern(dict_list, r'(?:ファイル:|file:|File:)([^|\]\}]+)')
    # print(Files[0])

    with open("/home/ryoma/nock100/3_Normal/Files.txt", mode='w') as file:
        file.write("\n".join(Files))
