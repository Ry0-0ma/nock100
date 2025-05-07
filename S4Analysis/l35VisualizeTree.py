# ライブラリに親しむ

from l33DependencyParsing import CaboChaParse, Modifier_Head
import CaboCha
import pydot

def visualize_dependency(Dependency:list, file_name:str):
    #                         有効グラフ            日本語フォント
    graph = pydot.Dot(graph_type='digraph', fontname="Noto Sans CJK JP") 
    for i, chunk in enumerate(Dependency): #添え字iと修飾の関係
        modifier = chunk['modifier']
        # i番目のノードをつくる
        graph.add_node(pydot.Node(i, label=modifier))
        if chunk['head'] != -1:
            # i番目のノードと修飾先のノードを矢印でつなげる
            graph.add_edge(pydot.Edge(i, chunk['head']))

    graph.write_png(file_name)
    print(file_name," を出力しました！")

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
    visualize_dependency(Dependency, 'DependencyTree.png')