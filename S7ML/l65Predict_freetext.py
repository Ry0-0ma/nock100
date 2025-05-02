# ライブラリに親しむ
import joblib
import pandas as pd

from collections import Counter
from sklearn.feature_extraction import DictVectorizer
from l61Feature import FeatureVector



def Text2Vector(text:str, vectorizer):
    words = text.split(' ')
    feature = dict(Counter(words))
    feature_vec = vectorizer.transform([feature])

    return feature_vec

if __name__ == "__main__":
    # 学習時のベクトル形式で、ベクトル化
    text = "the worst movie I 've ever seen"
    vectorizer = joblib.load('logistic_vec.pkl')
    feature_vec = Text2Vector(text, vectorizer)
    
    # ラベルを予想
    model = joblib.load('logistic_model.pkl')
    label = model.predict(feature_vec)

    print(f"{text} (predict: {label})")

    # the worst movie I 've ever seen (predict: [0])
