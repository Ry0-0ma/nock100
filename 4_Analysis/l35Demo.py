import CaboCha

def get_chunks(text):
    c = CaboCha.Parser()
    tree = c.parse(text)

    size = tree.size()
    chunks = {}
    tokens = []

    for i in range(size):
        token = tree.token(i)
        tokens.append(token)
        if token.chunk:
            chunks[i] = {
                "chunk": token.chunk,
                "tokens": [token.surface]
            }
        else:
            # 直前のchunkに所属する
            if chunks:
                last_key = list(chunks.keys())[-1]
                chunks[last_key]["tokens"].append(token.surface)

    results = []
    for i, data in chunks.items():
        chunk = data["chunk"]
        surface = ''.join(data["tokens"])
        results.append((i, surface, chunk.link))  # (文節番号, 表層文字列, 係り先の文節番号)

    return results


from sklearn.tree import DecisionTreeClassifier
from sklearn import tree
import matplotlib.pyplot as plt
import numpy as np

def visualize_dependency_tree(chunks):
    # ノード名（chunk surface）
    names = [chunk[1] for chunk in chunks]
    links = [chunk[2] for chunk in chunks]

    # 疑似的な訓練データ（ダミー）
    X = np.zeros((len(chunks), 1))
    y = np.array(links)

    clf = DecisionTreeClassifier(random_state=0)
    clf.fit(X, y)

    # ノード名を labels として指定
    fig, ax = plt.subplots(figsize=(12, 6))
    tree.plot_tree(clf, feature_names=["dummy"], class_names=names, filled=True, rounded=True, ax=ax)
    # plt.show()
    plt.savefig("DependencyTree.png")

if __name__ == "__main__":
    text = "メロスは激怒した。"
    chunks = get_chunks(text)
    visualize_dependency_tree(chunks)

