from gensim.models import KeyedVectors

if __name__== '__main__':
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    print(model.similarity('United_States', 'U.S.'))
    # (myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/S6WordVector$ python l51Similarity.py
    # 0.7310774