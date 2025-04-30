# 汎用コードをつくる のおかげ
from l20ReadJson import Read_Json
from l23Section import Extractpattern

import re


if __name__ == "__main__":
    #list - dict - key(title, text)
    dict_list = Read_Json("jawiki-country.json.gz")

    # ファイル:, file:, File: どれかの後から 
    # |, ], } のどれか までの間を抽出
    Files = Extractpattern(dict_list, r'(?:ファイル:|file:|File:)([^|\]\}]+)')
    # print(Files[0])

    with open("Files.txt", mode='w') as file:
        file.write("\n".join(Files))

"""
Coat_of_arms_of_Egypt.svg
Flag of Cairo.svg
Bilady, Bilady, Bilady.ogg
All Gizah Pyramids.jpg
Egyptiska hieroglyfer, Nordisk familjebok.png
ModernEgypt, Muhammad Ali by Auguste Couder, BAP 17996.jpg
"""