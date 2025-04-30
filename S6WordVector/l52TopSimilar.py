from gensim.models import KeyedVectors

def Print_Similarity(similar_words:list, object:str):
    print(f'「{object}」に類似した単語')
    for word, similarity in similar_words:
        print(f'{word}: {similarity}')

if __name__== '__main__':
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    # objectに類似度の高い単語を取得
    object = 'United_States'
    similar_words = model.most_similar(object, topn=10)
    Print_Similarity(similar_words, object)
    
"""
(myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/S6WordVector$ python l52TopSimilar.py
「United_States」に類似した単語
Unites_States: 0.7877249121665955
Untied_States: 0.7541369795799255
United_Sates: 0.7400726079940796
U.S.: 0.7310774326324463
theUnited_States: 0.6404393315315247
America: 0.6178411841392517
UnitedStates: 0.6167312860488892
Europe: 0.6132988333702087
countries: 0.6044804453849792
Canada: 0.6019068956375122
"""