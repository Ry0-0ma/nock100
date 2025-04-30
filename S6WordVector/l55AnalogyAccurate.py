# 無関係の下位問題を抽出する
# TODO: もっと高速にする(実行に時間かかりすぎ)
# 案: 取り出したセクションをTextから削除していく, Text短くなってく

import re
from gensim.models import KeyedVectors
from l54AnalogyData import ExtractSection, Vector_eachline
import time

# そのセクションの正解率を計算
def Accuracy_eachSection(section:str, Text:str, model:KeyedVectors):
    lines = ExtractSection(section, Text) #そのセクション内の行ごとのリスト
    
    # vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算
    # [1~4列目の単語, 計算したベクトルに最も似た単語, 類似度]
    SimilarLine = Vector_eachline(lines, model)
    
    # 正解率を計算
    correct = 0
    for line in SimilarLine:
        if line[4] == line[3]: #類似度最も高い単語と正解の単語が単語が一致
            correct += 1
    accuracy = correct / len(SimilarLine)
    return accuracy

# section に gram がついている: 文法的アナロジー
# それ以外 意味的アナロジー
def Print_Accuracy(titles:list, Text:str, model:KeyedVectors):
    SemanticAccuracy = [] #意味的アナロジー
    SyntacticAccuracy = [] #文法的アナロジー
    for section in titles:
        accuracy = Accuracy_eachSection(section, Text, model)
        print(f'{section} の正解率: {accuracy:.5%}')
        if 'gram' in section:
            SyntacticAccuracy.append(accuracy)
        else:
            SemanticAccuracy.append(accuracy)
    print(f'意味的アナロジーの平均正解率: {sum(SemanticAccuracy)/len(SemanticAccuracy):.5%}')
    print(f'文法的アナロジーの平均正解率: {sum(SyntacticAccuracy)/len(SyntacticAccuracy):.5%}')

if __name__ == "__main__":
    start_time = time.time()
    with open('questions-words.txt') as file:
        Text = file.read()
    # : で始まる行がセクションのタイトル
    titles = re.findall(r':\s*(.*)', Text)
    model = KeyedVectors.load('GoogleNews_WordVec.kv')
    Print_Accuracy(titles, Text, model)
    end_time = time.time()
    print(f'実行時間: {end_time - start_time:.2f}秒')
