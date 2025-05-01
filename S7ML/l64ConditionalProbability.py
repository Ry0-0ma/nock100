# ライブラリに親しむ
import pandas as pd
import joblib
from l61Feature import FeatureVector
from sklearn.feature_extraction import DictVectorizer

if __name__ == "__main__":
    # 検証データの先頭を抽出
    Develop = pd.read_csv('SST-2/dev.tsv', sep='\t', encoding='utf-8')
    Dev_dict = FeatureVector(Develop)
    feature = Dev_dict[0]['feature']
    trueLabel = Dev_dict[0]['label']
    # 学習時のベクトル形式で、ベクトル化
    vectorizer = joblib.load('logistic_vec.pkl')
    feature_matrix = vectorizer.transform([feature])

#  ここまでl63 と同じ 

    # 条件付き確率を計算
    model = joblib.load('logistic_model.pkl')
    prob = model.predict_proba(feature_matrix)
    print(f"positive(1): {prob[0][1]} negative(0): {prob[0][0]}")
