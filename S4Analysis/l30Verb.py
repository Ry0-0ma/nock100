# 11章1度に1つのことを
# やりすぎかも(ParseText の中に SplitParsedText をいれてもいいかも)
import MeCab

def ParseText(text: str)->str:
    # tagger = MeCab.Tagger("-d {}".format(MeCab.dict_path()))
    tagger = MeCab.Tagger('--rcfile=/etc/mecabrc -d /var/lib/mecab/dic/debian')
    return tagger.parse(text)

def SplitParsedText(parsed: str)->list:
    splited = []    
    for line in parsed.split('\n'):
        word = {}
        if line == 'EOS' or line == '':
            continue
        surface, features = line.split('\t')
        features = features.split(',')
        word["surface"] = surface
        word["features"] = features
        splited.append(word)    

    return splited

def ExtractVerbs(text: str)->list:
    verbs = []
    parsed = ParseText(text)
    for word in SplitParsedText(parsed):
        if word["features"][0] == '動詞':
            verbs.append(word["surface"])

    return verbs

if __name__ == "__main__":
    text = """
    メロスは激怒した。
    必ず、かの邪智暴虐の王を除かなければならぬと決意した。
    メロスには政治がわからぬ。
    メロスは、村の牧人である。
    笛を吹き、羊と遊んで暮して来た。
    けれども邪悪に対しては、人一倍に敏感であった。
    """
    print(ParseText(text))

    verbs = ExtractVerbs(text)
    print("抽出された動詞:", verbs)


# 抽出された動詞: ['し', '除か', 'なら', 'し', 'わから', '吹き', '遊ん', '暮し', '来']


    """
    tagger.parse で実行していた
    # print(type(ParseText(text))) : str
    print(ParseText(text))
        メロス  名詞,一般,*,*,*,*,*
        は      助詞,係助詞,*,*,*,*,は,ハ,ワ
        激怒    名詞,サ変接続,*,*,*,*,激怒,ゲキド,ゲキド
        し      動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
        た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
        。      記号,句点,*,*,*,*,。,。,。
        
        中略
        surfece\t  features[0],features[2]...\n

        。      記号,句点,*,*,*,*,。,。,。
        EOS
    """
    """
    表層系  品詞 品詞細分類1,2,3, 活用型、活用形、原型、読み、発音
    """
    """
    def ParseToNode(text: str):
        # tagger = MeCab.Tagger("-d {}".format(MeCab.dict_path()))
        tagger = MeCab.Tagger('--rcfile=/etc/mecabrc -d /var/lib/mecab/dic/debian')
        tagger.parse('')  # Python バグ対策（必要）
        node = tagger.parseToNode(text)
        return node

    def ExtractVerbs(text: str):
        verbs = []
        # for node in ParseToNode(text):
        # ノードオブジェクトは、単方向リスト(not iterable)なのでfor文使えない
        node = ParseToNode(text)
        while node:
            print(node.surface)
            if '動詞' in node.feature:
                verbs.append(node.surface)
            node = node.next
        
        print("last node:", node)

        return verbs
    """

    