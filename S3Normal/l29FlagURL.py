# 10章無関係の下位問題を抽出する
from l25ExtractTemplate import ReturnInfo_dictlist
import requests

#MediaWiki APIのテンプレートに従った
def ObtainFlagURL(FlagFile:str):
    S = requests.Session() #APIリクエスト用のセッションを作成
    URL = "https://en.wikipedia.org/w/api.php" #MediaWiki API
    title = "File:"+FlagFile
    PARAMS = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": title,
        "iiprop": "url" #URLを取得するkey
    }
    #Getリクエストを送り、レスポンスをJSONとしてパース(必要な情報だけ抽出)
    R = S.get(url=URL, params=PARAMS) 
    DATA = R.json()

    PAGES = DATA["query"]["pages"]
    for page in PAGES.values():
        if "imageinfo" in page:
            return page["imageinfo"][0]["url"]

def AllFlagURL(Info_dictlist:list):
    FlagURL = []
    for info_dict in Info_dictlist:
        if "国旗画像" in info_dict.keys():
            FlagURL.append(ObtainFlagURL(info_dict["国旗画像"]))
    return FlagURL

if __name__ == "__main__":
    # 記事ごとに基礎情報の辞書オブジェクトが格納されたリスト
    Info_dictlist = ReturnInfo_dictlist()
    FlagURL = AllFlagURL(Info_dictlist)
    print(FlagURL)
    

# print(FlagURL[0])
# https://upload.wikimedia.org/wikipedia/commons/f/fe/Flag_of_Egypt.svg