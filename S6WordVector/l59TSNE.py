from gensim.models import KeyedVectors
from sklearn.manifold import TSNE
import numpy as np
import matplotlib.pyplot as plt
from l57k_means import ExtractCountry, Kmeans_WordVec


def PlotTSNE(model, World:list, labels:list):
    # 単語ベクトルを取得
    WordVec = []
    for country in World:
        WordVec.append(model[country])
    # t-SNEの入力はnumpyかpandasのDataFrame
    WordVec = np.array(WordVec)
    # t-SNEで次元削減
    tsne = TSNE(n_components=2, random_state=0)
    WordVec_2D = tsne.fit_transform(WordVec)

    # プロット
    plt.figure()
    # 散布図を描画               データ点の色はlabelsに基づき、カラーマップがviridis、透明度が0.5 
    scatter = plt.scatter(WordVec_2D[:, 0], WordVec_2D[:, 1], c=labels, cmap='viridis', alpha=0.5)
    plt.colorbar(scatter)
    plt.title('t-SNE Visualization of Country Word Vectors')
    plt.xlabel('t-SNE Component 1')
    plt.ylabel('t-SNE Component 2')
    plt.savefig('tSNE_WordVec.png')
    plt.close()


if __name__ == "__main__":
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    World = ExtractCountry(model)
    labels = Kmeans_WordVec(model, World)
    PlotTSNE(model, World, labels)


"""
TSNEのパラメータ
n_components: 次元数
random_state: デフォNone->毎回異なる結果, 0:同じ結果
perplexity:近傍サイズ, 小さい:局所的, 大きい:大域的
n_iter: デフォルト1000
learning_rate: 200
metric: 距離の計の計算, デフォルトeuclidean
init: 初期配置, デフォルトrandom
verbose: 進捗状況を出力するかどうか
"""