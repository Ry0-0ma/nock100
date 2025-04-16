# p51. コードを段落に分ける(Make_dictlist)

from l20ReadJson import Read_Json, ExtractJornal_byWord
import re

#基礎情報テンプレートを抜き出す
def ExtractTemplate(Jornals:list)->list:
    Templates = []
    for jornal in Jornals:
        # 基礎情報 の後に | が来た後からの内容を取り出す。
        # 終わりは、\n}}
        Templates += re.findall(r'\{\{基礎情報 国\n(.*?)\n\}\}', jornal['text'], re.DOTALL) #re.DOTALLで.に改行を含む

    return Templates #記事ごとのリスト

def Make_dictlist(Templates:list)->list:
    #取り出したテンプレートをそれぞれkeyとvalueに分ける
    KeyValue = []
    for element in Templates:
        # = より前をkey, = より後をvalue
        pattern = r'\|(.*?)\s*=\s*(.*?)\n'
        KeyValue.append(re.findall(pattern, element))
    # Informationの要素:(key, value)の要素を持つリスト -> (list-list-list(key,value))

    # 記事ごとに辞書を作成
    Info_dictlist = []
    for info in KeyValue:
        Info_dict = {}
        for key, value in info:
            Info_dict[key] = value
        Info_dictlist.append(Info_dict)
    # Info_dictlist には、各記事の辞書オブジェクト
    return Info_dictlist

def ReturnInfo_dictlist(): #後の問題でもInfo_dictlistを使うための関数
    #list - dict - key(title, text)
    dict_list = Read_Json("/home/ryoma/nock100/3_Normal/jawiki-country.json.gz")
    Jornals = ExtractJornal_byWord(dict_list, 'イギリス')
    Templates = ExtractTemplate(Jornals)
    Info_dictlist = Make_dictlist(Templates)
    return Info_dictlist


if __name__ == "__main__":
    #list - dict - key(title, text)
    dict_list = Read_Json("/home/ryoma/nock100/3_Normal/jawiki-country.json.gz")
    Jornals = ExtractJornal_byWord(dict_list, 'イギリス') #イギリスに関する記事のみ抜き出した

    Templates = ExtractTemplate(Jornals)
    Info_dictlist = Make_dictlist(Templates)
    # print(Info_dictlist[0]['略名'])
    # print(Info_dictlist[3])

    print(Info_dictlist)



# r'\{\{基礎情報.*?\|(.*?)\n\}\}', jornal['text']