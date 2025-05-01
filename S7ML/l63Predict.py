# ライブラリに親しむ
import joblib
from l61Feature import FeatureVector
from sklearn.feature_extraction import DictVectorizer
import pandas as pd

if __name__ == "__main__":
    # 検証データの先頭を抽出
    Develop = pd.read_csv('SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = FeatureVector(Develop)
    feature = Dev_dict[0]['feature']
    trueLabel = Dev_dict[0]['label']

    # 学習時のベクトル形式で、ベクトル化
    vectorizer = joblib.load('logistic_vec.pkl')
    feature_matrix = vectorizer.transform([feature])
    
    # ラベルを予想
    model = joblib.load('logistic_model.pkl')
    label = model.predict(feature_matrix)

    print(f"true: {trueLabel} predict: {label}")

    # true: 1 predict: [1]