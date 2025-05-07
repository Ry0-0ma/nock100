# p.114 制御フローを削除する(できなかった)
# l33と共通の部分が多い->上手いこと再利用できたかも
# p.60 自分の考えを記録する

from l33DependencyParsing import CaboChaParse

# 動詞が含まれている句を取り出す
def VerbPhrase(ParsedLines, line_idx)->(str,int,bool):
    increment = 0
    phrase = ''
    IncludeVerb = False
    for line in ParsedLines[line_idx:]:
        #修飾の行、文末、空白までが句
        if line[0] == '*' or line == 'EOS' or line == '':
            return phrase, increment, IncludeVerb
        surface, features = line.split('\t')
        features = features.split(',')
        if features[0] == '動詞':
            IncludeVerb = True        
        phrase += surface
        increment += 1

def ExtractPredicate(parsed: str): #述語
    Predicate = []
    ParsedLines = parsed.split('\n')
    line_idx = 0
    while line_idx < len(ParsedLines):
        line = ParsedLines[line_idx]
        # 文末だけでなく、修飾の行も飛ばす
        if line == 'EOS' or line == '' or line[0] == '*':
            line_idx += 1
            continue
        phrase, increment, IsVerb = VerbPhrase(ParsedLines, line_idx)
        if IsVerb:
            Predicate.append(phrase)
        line_idx += increment

    return Predicate

# def MelosPredict(Dependency:list, Predicate:list):
"""
    メロスは         激怒した。
    激怒した。       決意した。
    
    のように 述語   述語 の場合は、同じ主語っぽい
"""

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
    Predicate = ExtractPredicate(parsed)
    print(Predicate)

    # ['激怒した。', '除かなければならぬと', '決意した。', 'わからぬ。', '吹き、', '遊んで', '暮して来た。']

    # これだと主語の関係を使ってない
    # この文だと全部の述語の主語メロスっぽいからこれで
   