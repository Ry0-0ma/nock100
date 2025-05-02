import pandas as pd
import joblib
import matplotlib.pyplot as plt

from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction import DictVectorizer
from sklearn.metrics import accuracy_score

from l61Feature import FeatureVector
from l62logisticRegression import Feature_Label


def Accuracy_byC(C_list:list, Train_matrix, TrainLabels, Dev_matrix, DevLabels)->list:
    Accuracy_list = []
    for param_C in C_list:
        # 正則化パラメータを変えて学習
        model = LogisticRegression(max_iter=2000, C=param_C)
        model.fit(Train_matrix, TrainLabels)

        labels = model.predict(Dev_matrix)
        Accuracy_list.append(accuracy_score(DevLabels, labels))
    
    return Accuracy_list

def PlotAccuracy(C_list:list, Accuracy_list:list):
    plt.figure()
    plt.plot(C_list, Accuracy_list)
    plt.xscale('log')  # x軸を対数スケールに設定
    plt.xlabel('Inverse of regularization strength: C (log Scale)')
    plt.ylabel('Accuracy Rate')
    plt.title('Accuracy vs Regularization Strength')
    plt.savefig('AccuracyRate_Dev.png')

def Matrix_Label(path:str, vectorizer):
    dataframe = pd.read_csv(path, sep='\t', encoding='utf-8')
    dict_list = FeatureVector(dataframe)
    feature, truelabels = Feature_Label(dict_list)
    feature_matrix = vectorizer.transform(feature)

    return feature_matrix, truelabels


if __name__ == "__main__":
    vectorizer = joblib.load('logistic_vec.pkl')
    Train_matrix, TrainLabels = Matrix_Label('SST-2/train.tsv', vectorizer)
    Dev_matrix, DevLabels = Matrix_Label('SST-2/dev.tsv', vectorizer)

    C_list = [0.01, 0.1, 1.0, 10, 100] #デフォルトは1.0
    Accuracy_list = Accuracy_byC(C_list, Train_matrix, TrainLabels, Dev_matrix, DevLabels)

    PlotAccuracy(C_list, Accuracy_list)

