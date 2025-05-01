# ライブラリに親しむ
from l61Feature import FeatureVector
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
import pandas as pd
import joblib

def Feature_Label(dict_list:list)->(list, list):
    features = []
    labels = []
    for dictionary in dict_list:
        features.append(dictionary['feature'])
        labels.append(dictionary['label'])
    return features, labels

if __name__ == "__main__":
    Train = pd.read_csv('SST-2/train.tsv', sep='\t', encoding='utf-8')
    Train_dict = FeatureVector(Train)
    features, labels = Feature_Label(Train_dict)

     # 辞書形式をベクトル形式に変換
    vectorizer = DictVectorizer(sparse=True)  # スパース行列として保持
    feature_matrix = vectorizer.fit_transform(features)

    model = LogisticRegression(max_iter=300) #デフォルトは100
    model.fit(feature_matrix, labels)
    joblib.dump(model, 'logistic_model.pkl')
    joblib.dump(vectorizer, 'logistic_vec.pkl')  # 保存

