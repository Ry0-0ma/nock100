# p.135 汎用コードをたくさんつくる
from l30Verb import ParseText, SplitParsedText, ExtractVerbs
import MeCab

def Extract_feature(text: str, idx_feature: int)->list:
    feature = []
    parsed = ParseText(text)
    for word in SplitParsedText(parsed):
        if word["features"][0] == '動詞':
            feature.append(word["features"][idx_feature])

    return feature

if __name__ == "__main__":
    text = """
    メロスは激怒した。
    必ず、かの邪智暴虐の王を除かなければならぬと決意した。
    メロスには政治がわからぬ。
    メロスは、村の牧人である。
    笛を吹き、羊と遊んで暮して来た。
    けれども邪悪に対しては、人一倍に敏感であった。
    """
    verbs = ExtractVerbs(text)
    baseform = Extract_feature(text, 6) #7番目の特徴が原型

    for verb, base in zip(verbs, baseform):
        print("動詞: ", verb, "\t原型: ", base)

    """
    動詞:  し       原型:  する
    動詞:  除か     原型:  除く
    動詞:  なら     原型:  なる
    動詞:  し       原型:  する
    動詞:  わから   原型:  わかる
    動詞:  吹き     原型:  吹く
    動詞:  遊ん     原型:  遊ぶ
    動詞:  暮し     原型:  暮す
    動詞:  来       原型:  来る
    """


