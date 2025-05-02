import pandas as pd
import joblib
from l61Feature import FeatureVector
from l62logisticRegression import Feature_Label

from sklearn.metrics import accuracy_score
from sklearn.metrics import precision_score
from sklearn.metrics import recall_score
from sklearn.metrics import f1_score

def Metrics4(dict_list:list, vectorizer, model):
    features, truelabels = Feature_Label(dict_list)
    feature_matrix = vectorizer.transform(features)
    labels = model.predict(feature_matrix)

    print(f"正解率: {accuracy_score(truelabels, labels)}")
    print(f"適合率: {precision_score(truelabels, labels)}")
    print(f"再現率: {recall_score(truelabels, labels)}")
    print(f"F1スコア: {f1_score(truelabels, labels)}")


if __name__ == "__main__":
    model = joblib.load('logistic_model.pkl')
    vectorizer = joblib.load('logistic_vec.pkl')
    
    print("学習データのスコア")
    Train = pd.read_csv('SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = FeatureVector(Train)
    Metrics4(Train_dict, vectorizer, model)

    print("検証データのスコア")
    Develop = pd.read_csv('SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = FeatureVector(Develop)
    Metrics4(Dev_dict, vectorizer, model)

    """
学習データのスコア
正解率: 0.9427756908046148
適合率: 0.9433967226912859
再現率: 0.9546966914211185
F1スコア: 0.9490130708578082
検証データのスコア
正解率: 0.8107798165137615
適合率: 0.7987152034261242
再現率: 0.8400900900900901
F1スコア: 0.818880351262349
    """