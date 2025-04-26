# 無関係の下位問題を抽出する
from l40Zero_Shot import FetchAnswer_gemini
from l42AccuracyRate import SplitQustion_Option, CreatePrompt, ExtractAnswer, AccuracyRate
import random

def PrintAccuracyRate(Response:str, Questions:list):
    Answers = ExtractAnswer(Response)
    accuracy_rate = AccuracyRate(Answers, Questions)
    print(f"Accuracy Rate: {accuracy_rate}%")

# 問題の順番を変えた場合
def Accuracy_ShuffleQuestion(Questions:list):
    random.shuffle(Questions) # 質問をシャッフル
    prompt = CreatePrompt(Questions)
    Response = FetchAnswer_gemini(prompt, MaxOutputTokens=2500)
    print(f"\n Shuffle \n {Response}") # l43GeminiAnswers.txt
    PrintAccuracyRate(Response, Questions)

# 生成のパラメータを変えた場合
def Accuracy_ChangedPameter(
        Questions:list,
        MaxOutputTokens:int=2500, 
        Temperture:float=0.5,
        TopP:float=0.80,
        TopK:int=10
    ):
    prompt = CreatePrompt(Questions)
    Response = FetchAnswer_gemini(
        prompt=prompt, 
        MaxOutputTokens=MaxOutputTokens,
        Temperature=Temperture,
        TopP=TopP,
        TopK=TopK
    )
    print(f"\n ChangedParameter \n {Response}") # l43GeminiAnswers.txt
    PrintAccuracyRate(Response, Questions)

def Questions_SameAnswer(Questions:list, same:str):
    # 質問の正解が同じものを抽出する
    SameAnswers = []
    for question in Questions:
        if question['Correct'] == same:
            SameAnswers.append(question)
    return SameAnswers

# 同じ正解の問題しかない場合(問題が少なくなったから、geminiの出力が変わっている)
def Accuracy_SameAnswer(Questions:list, same:str):
    SameAnswers = Questions_SameAnswer(Questions, same) 
    prompt = CreatePrompt(SameAnswers)
    Response = FetchAnswer_gemini(prompt, MaxOutputTokens=2500)
    print(f"\n SameAnswer \n {Response}") #l43GeminiAnswers.txt
    
    geminiAnswers = Response.split('\n')
    correct_count = 0
    for answer in geminiAnswers:
        if same in answer:
            correct_count += 1
    accuracy_rate = correct_count / len(geminiAnswers) * 100
    print(f"Accuracy Rate: {accuracy_rate}%")

if __name__ == "__main__":
    with open('/home/ryoma/nock100/S5LLM/japanese_history.csv') as file:
        lines = file.readlines()

    # 問題の順序を変える、パラメータを変える、同じ答えの問題を集めた場合 の3通り
    Questions = SplitQustion_Option(lines)
    Accuracy_SameAnswer(Questions, 'D') #Accuracy Rate: 81.13207547169812%
    Accuracy_ChangedPameter(Questions)  #Accuracy Rate: 89.33333333333333%
    Accuracy_ShuffleQuestion(Questions) #Accuracy Rate: 88.0%