# 10章無関係の下位問題を抽出
from l30Verb import ParseText, SplitParsedText
import MeCab

# 「AのB」の形の名詞句
def ConnctNoun(words:list, idx:int)->bool:
    if words[idx+1]["features"][0] == '助詞' and words[idx+1]["surface"] == 'の':
        if words[idx]["features"][0] == '名詞' and words[idx+2]["features"][0] == '名詞':
            return True
    return False

def Extract_ConnectedNoun(text: str):
    Nouns = []
    parsed = ParseText(text)
    words = SplitParsedText(parsed)
    for i in range(len(words)-2):
        if ConnctNoun(words, i):
            Nouns.append([words[i]["surface"], words[i+2]["surface"]])
    return Nouns

if __name__ == "__main__":
    text = """
    メロスは激怒した。
    必ず、かの邪智暴虐の王を除かなければならぬと決意した。
    メロスには政治がわからぬ。
    メロスは、村の牧人である。
    笛を吹き、羊と遊んで暮して来た。
    けれども邪悪に対しては、人一倍に敏感であった。
    """
    print(Extract_ConnectedNoun(text))