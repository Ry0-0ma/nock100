from l33DependencyParsing import CaboChaParse
import CaboCha
import pydot

# chunk:意味のあるまとまり
def get_chunks(cabocha_str):
    chunks = []
    chunk = {'tokens': [], 'dst': -1}

    for line in cabocha_str.split('\n'):
        if line == 'EOS' or line == '':
            if chunk['tokens']:  # 最後のチャンク
                chunks.append(chunk)
            break

        if line.startswith('*'):
            if chunk['tokens']:  # チャンク切り替え
                chunks.append(chunk)
                chunk = {'tokens': [], 'dst': -1}
            parts = line.split()
            chunk['dst'] = int(parts[2].rstrip('D'))  # 係り先のチャンク番号
        else:
            surface = line.split('\t')[0]
            chunk['tokens'].append(surface)

    return chunks

def visualize_dependency(chunks, file_name:str):
    graph = pydot.Dot(graph_type='digraph', fontname="Noto Sans CJK JP")

    for i, chunk in enumerate(chunks):
        chunk_text = ''.join(chunk['tokens'])
        graph.add_node(pydot.Node(i, label=chunk_text))
        if chunk['dst'] != -1:
            dst_text = ''.join(chunks[chunk['dst']]['tokens'])
            graph.add_edge(pydot.Edge(i, chunk['dst']))

    graph.write_png(file_name)
    print(file_name," を出力しました！")

if __name__ == "__main__":
    text = "メロスは激怒した。"
    # text = """
    # メロスは激怒した。
    # 必ず、かの邪智暴虐の王を除かなければならぬと決意した。
    # メロスには政治がわからぬ。
    # メロスは、村の牧人である。
    # 笛を吹き、羊と遊んで暮して来た。
    # けれども邪悪に対しては、人一倍に敏感であった。
    # """
    cabocha_result = CaboChaParse(text)
    chunks = get_chunks(cabocha_result)
    visualize_dependency(chunks, 'dependency_tree.png')