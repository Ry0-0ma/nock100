from gensim.models import KeyedVectors
from l52TopSimilar import Print_Similarity

def Add_WordVec(model, object:str, sub:str, add:str):
        return model[object] - model[sub] + model[add]
    
if __name__== '__main__':
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    # Spain - Madrid + Athens
    # スペインにとってのマドリードは、アテネにとって何?
    Added_Vec = Add_WordVec(model, object='Spain', sub='Madrid', add='Athens')
    similar_words = model.similar_by_vector(Added_Vec, topn=10)
    Print_Similarity(similar_words, 'Spain - Madrid + Athens')

    """
    「Spain - Madrid + Athens」に類似した単語
    Athens: 0.7528455853462219
    Greece: 0.6685471534729004
    Aristeidis_Grigoriadis: 0.5495777726173401
    Ioannis_Drymonakos: 0.5361456871032715
    Greeks: 0.5351787805557251
    Ioannis_Christou: 0.5330225825309753
    Hrysopiyi_Devetzi: 0.5088489651679993
    Iraklion: 0.5059264302253723
    Greek: 0.5040616393089294
    Athens_Greece: 0.503411054611206
    """