import pandas as pd
import joblib

from l61Feature import FeatureVector
from l62logisticRegression import Feature_Label

from sklearn.metrics import confusion_matrix

def Dict2Confusion(dict_list:list, vectorizer, model):
    features, truelabels = Feature_Label(dict_list)
    feature_matrix = vectorizer.transform(features)
    labels = model.predict(feature_matrix)

    confu_MX = confusion_matrix(truelabels, labels)
    return confu_MX

if __name__ == "__main__":
    Develop = pd.read_csv('SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = FeatureVector(Develop)
    model = joblib.load('logistic_model.pkl')
    vectorizer = joblib.load('logistic_vec.pkl')

    confu_MX = Dict2Confusion(Dev_dict, vectorizer, model)
    
    print(confu_MX)

"""
        予想値
       0     1
真 0  真陰　偽陽
値 1  偽陰　真陽
"""
"""
[[334  94]
 [ 71 373]]
"""

