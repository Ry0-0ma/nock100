import re
from gensim.models import KeyedVectors
from l53Add_WordVec import Add_WordVec


def ExtractSection(section:str, Text:str)->list:
    # 正規表現でセクションを抽出する(セクションは : で始まる)
    content = re.search(rf'{section}\s*(.*?)(?=:|$)', Text, re.DOTALL)
    lines = content.group(1).split('\n')
    return lines

# vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算
def Vector_eachline(lines: list, model):
    SimilarLine = []
    for line in lines:
        words = line.split(' ')
        if len(words) == 4:
            Vec_line = Add_WordVec(model, object=words[1], sub=words[0], add=words[2])
            
            MostSimilar = model.similar_by_vector(Vec_line, topn=2)
            similar_word, similarity = MostSimilar[0]
            # #足した単語(3列目)と同じのときは、2番目に類似度の高い単語に
            if similar_word == words[2]: #例: Greece - Athens + Baghdad = Baghdad
                similar_word, similarity = MostSimilar[1]

            SimilarLine.append([words[0], words[1], words[2], words[3], similar_word, similarity])
    return SimilarLine

def Print_Similarity(SimilarLine: list):
    print(f'2列目 - 1列目 + 3列目 = 最も似た単語:類似度, 正解の単語')
    for line in SimilarLine: 
        print(f'{line[1]} - {line[0]} + {line[2]} = {line[4]}: {line[5]}, 正解({line[3]})')

if __name__ == "__main__":
    with open('questions-words.txt') as file:
        Text = file.read()
    lines = ExtractSection(': capital-common-countries', Text)
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    SimilarLine = Vector_eachline(lines, model)
    Print_Similarity(SimilarLine)

""" l54AnalogyLines.txt
2列目 - 1列目 + 3列目 = 最も似た単語:類似度, 正解の単語
Greece - Athens + Baghdad = Baghdad: 0.7489827275276184, 正解(Iraq)
Greece - Athens + Bangkok = Bangkok: 0.7431141138076782, 正解(Thailand)
Greece - Athens + Beijing = China: 0.7186591029167175, 正解(China)
Greece - Athens + Berlin = Germany: 0.6720892190933228, 正解(Germany)
Greece - Athens + Bern = Bern: 0.6902341842651367, 正解(Switzerland)
Greece - Athens + Cairo = Egypt: 0.7626821994781494, 正解(Egypt)
"""
    

# http://download.tensorflow.org/data/questions-words.txt

