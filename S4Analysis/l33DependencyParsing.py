# 10章無関係の下位問題を抽出する
# p.135 汎用コードをつくる
# p.91 関数から早く返す

import CaboCha

def CaboChaParse(text:str)->list:
    cabocha = CaboCha.Parser()
    return cabocha.parse(text).toString(CaboCha.FORMAT_LATTICE)

# 句を抽出し、その過程でのline_idxの増分も返す
def ExtractPhrase(ParsedLines:list, line_idx:int)->(str,int):
    line = ParsedLines[line_idx]
    increment = 0
    phrase = ''
    for line in ParsedLines[line_idx:]:
        #修飾の行、文末、空白までが句
        if line[0] == '*' or line == 'EOS' or line == '':
            return phrase, increment
        surface, features = line.split('\t')
        phrase += surface
        increment += 1

# 修飾元の句と修飾先の句番号を返す
def Modifier_Head(parsed: str)->list: #修飾元_修飾先
    Dependency = []
    ParsedLines = parsed.split('\n')
    line_idx = 0
    while line_idx < len(ParsedLines):
        line = ParsedLines[line_idx]
        if line == 'EOS' or line == '':
            line_idx += 1
            continue
        if line[0] == '*': #修飾を表す行のとき
            modify = line.split(' ') #* 0 1D 0/1 1.594535
            head = int(modify[2][:-1]) #修飾先の番号
            line_idx += 1
        else: #句とその句の修飾先を格納
            phrase, increment = ExtractPhrase(ParsedLines, line_idx)
            Dependency.append({'modifier':phrase, 'head':head})
            line_idx += increment
    return Dependency

def Print_ModifierHead(Dependency:list):
    for modify in Dependency:
        modifier = modify['modifier']
        head_num = modify['head']
        if head_num == -1:
            head = ''
        else:
            head = Dependency[head_num]['modifier']
        print(modifier,"\t", head)


if __name__ == "__main__":
    text = """
    メロスは激怒した。
    必ず、かの邪智暴虐の王を除かなければならぬと決意した。
    メロスには政治がわからぬ。
    メロスは、村の牧人である。
    笛を吹き、羊と遊んで暮して来た。
    けれども邪悪に対しては、人一倍に敏感であった。
    """
    parsed = CaboChaParse(text)
    Dependency = Modifier_Head(parsed)
    Print_ModifierHead(Dependency)

    """
メロスは         激怒した。
激怒した。       決意した。
必ず、   除かなければならぬと
かの     邪智暴虐の
邪智暴虐の       王を
王を     除かなければならぬと
除かなければならぬと     決意した。
決意した。       わからぬ。
メロスには       わからぬ。
政治が   わからぬ。
わからぬ。       牧人である。
メロスは、       牧人である。
村の     牧人である。
牧人である。     暮して来た。
笛を     吹き、
吹き、   暮して来た。
羊と     遊んで
遊んで   暮して来た。
暮して来た。     敏感であった。
けれども         敏感であった。
邪悪に対しては、         敏感であった。
人一倍に         敏感であった。
敏感であった。
    """

    """
    print(cabocha.parse(text).toString(CaboCha.FORMAT_LATTICE))
    * 0 1D 0/1 1.594535
    メロス  名詞,一般,*,*,*,*,*
    は      助詞,係助詞,*,*,*,*,は,ハ,ワ
    * 1 7D 1/2 1.020422
    激怒    名詞,サ変接続,*,*,*,*,激怒,ゲキド,ゲキド
    し      動詞,自立,*,*,サ変・スル,連用形,する,シ,シ
    た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
    。      記号,句点,*,*,*,*,。,。,。
    * 2 6D 0/0 0.435788
    必ず    副詞,助詞類接続,*,*,*,*,必ず,カナラズ,カナラズ
    、      記号,読点,*,*,*,*,、,、,、
    * 3 4D 0/0 1.042410

    中略

    * 22 -1D 0/3 0.000000
    敏感    名詞,形容動詞語幹,*,*,*,*,敏感,ビンカン,ビンカン
    で      助動詞,*,*,*,特殊・ダ,連用形,だ,デ,デ
    あっ    助動詞,*,*,*,五段・ラ行アル,連用タ接続,ある,アッ,アッ
    た      助動詞,*,*,*,特殊・タ,基本形,た,タ,タ
    。      記号,句点,*,*,*,*,。,。,。
    EOS
    """

    """
     print(cabocha.parseToString(text))

    メロスは-D
            激怒した。-----------D
                  必ず、-------D |
                      かの-D   | |
                  邪智暴虐の-D | |
                          王を-D |
            除かなければならぬと-D
                        決意した。-----D
                          メロスには---D
                                政治が-D
                              わからぬ。-----D
                                メロスは、---D
                                        村の-D
                                  牧人である。---------D
                                            笛を-D     |
                                            吹き、-----D
                                                羊と-D |
                                                遊んで-D
                                            暮して来た。-------D
                                                  けれども-----D
                                            邪悪に対しては、---D
                                                      人一倍に-D
                                                  敏感であった。    
    """