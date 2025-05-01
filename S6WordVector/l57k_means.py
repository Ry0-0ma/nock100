from sklearn.cluster import KMeans
from gensim.models import KeyedVectors
from l54AnalogyData import ExtractSection

# 国名を抽出
def ExtractCountry(model):
    with open('questions-words.txt') as file:
        text = file.read()
    lines = ExtractSection(': capital-world', text)
    World = set()
    for line in lines:
        countries = line.split(' ')
        for country in countries:
            # 単語ベクトルを取得できる国名のみ追加
            try:
                model[country]
                World.add(country)
            except KeyError:
                continue
    return list(World)

def Kmeans_WordVec(model, World:list):
    # 単語ベクトルを取得
    WordVec = []
    for country in World:
        try:
            WordVec.append(model[country])
        except KeyError:
            continue
    # KMeansクラスタリング
    kmeans = KMeans(n_clusters=5, random_state=0).fit(WordVec)
    # クラスタリング結果を取得
    labels = kmeans.labels_
    return labels

def Print_Labels(labels:list, World:list):
    # クラスタリング結果を表示
    for country, label in zip(World, labels):
        print(f'{country}: {label}')

if __name__ == "__main__":
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    World = ExtractCountry(model)
    # for country in World:
    #     print(country)
    Labels = Kmeans_WordVec(model, World)
    Print_Labels(Labels, World)