# ライブラリに親しむ
# 
import joblib
import pandas as pd


def SortWeight(model, vectorizer)->list:
    weight = model.coef_[0] #2値分類は一次元
    FeatureNames = vectorizer.get_feature_names()

    # 重みと特徴量の名前をペアにして、降順にソート
    sorted_feature = sorted(zip(FeatureNames, weight), key=lambda x: x[1], reverse=True)
    return sorted_feature

def Print_TopWeight(sorted_feature:list, topN:int=20):
    print(f"Top {topN}")
    for weight, name in sorted_feature[:topN]:
        print(f"{name}: {weight}")

def Print_BottomWeight(sorted_feature:list, bottomN:int=20):
    print(f"Bottom {bottomN}")
    for weight, name in sorted_feature[-bottomN:]:
        print(f"{name}: {weight}")


if __name__ == "__main__":
    model = joblib.load('logistic_model.pkl')
    vectorizer = joblib.load('logistic_vec.pkl')

    sorted_feature = SortWeight(model, vectorizer)
    Print_TopWeight(sorted_feature)
    Print_BottomWeight(sorted_feature)
    
"""
Top 20
3.4793405936040296: refreshing
3.4744062013596317: remarkable
3.2539750843771458: powerful
3.191817878484329: hilarious
3.008063823517821: beautiful
2.9949621755955786: wonderful
2.93223212863145: prose
2.9235269041937006: terrific
2.8797836994869663: treat
2.8632770500432296: appealing
2.829150173499692: enjoyable
2.781304834264385: charmer
2.7225078048464426: vividly
2.704763936495556: likable
2.6361930575610075: charming
2.6355117836301996: solid
2.615504489892426: impressive
2.5875544847392042: fascinating
2.5864359260142384: half-bad
2.5577990290574495: intriguing
Bottom 20
-2.9682450434726437: unfortunately
-3.005807092809074: pointless
-3.0132151215614873: poor
-3.0139645094967973: lousy
-3.019511077839: hardly
-3.024155913040201: none
-3.0500737825478166: squanders
-3.07862884441608: lack
-3.192910398575266: waste
-3.21625607093393: loses
-3.217458849416687: depressing
-3.229029312943354: flat
-3.302096930853841: bore
-3.3730345917719577: stupid
-3.643717738013141: failure
-3.6980639002340996: mess
-3.706498553382559: devoid
-4.019603623221787: worst
-4.088141539879332: lacks
-4.356955226169872: lacking
"""