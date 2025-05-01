import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from gensim.models import KeyedVectors
from l57k_means import ExtractCountry

def PlotDendrogram(linkage_matrix, label:list, output_file:str):
    # デンドログラムを描画(樹形図)
    plt.figure()
    dendrogram(linkage_matrix, labels=label)
    plt.title('Ward Clustering: Country Word Vectors')
    plt.xlabel('Countries')
    plt.ylabel('Distance')
    plt.savefig(output_file)
    plt.close()

def WardClustering(model, World:list, output_file:str):
    # 単語ベクトルを取得
    WordVec = []
    for country in World:
        WordVec.append(model[country])
        
    # 階層的クラスタリング
    linkage_matrix = linkage(WordVec, method='ward')
    # デンドログラムを描画
    PlotDendrogram(linkage_matrix, World, output_file)
    

if __name__ == "__main__":
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    World = ExtractCountry(model)
    WardClustering(model, World, 'WardClustering.png')
