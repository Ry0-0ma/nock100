# 11章1度に1つのことを
from l40Zero_Shot import FetchAnswer_gemini
import re

def SplitQustion_Option(lines:list)->list:
    Questions = []
    pattern = re.compile(r"(.*),(.*?),(.*?),(.*?),(.*?),(.)")
    for line in lines:
        Match = re.search(pattern, line)
        question, optionA, optionB, optionC, optionD, correct = Match.groups()
        Questions.append({'Q': question, 'A': optionA, 'B': optionB, 'C': optionC, 'D': optionD, 'Correct': correct})

    return Questions

def CreatePrompt(Questions:list)->str:
    prompt = ""
    for question in Questions:
        prompt += f"{question['Q']}\n"
        prompt += f"A　{question['A']}\n"
        prompt += f"B　{question['B']}\n"
        prompt += f"C　{question['C']}\n"
        prompt += f"D　{question['D']}\n"
        prompt += "解答: \n"
    return prompt

# geminiの問題への解答を抽出
def ExtractAnswer(Response:str)->list:
    # pattern = re.compile(r"解答:\s*([A-D])")
    pattern = re.compile(r"\*\*([A-D])\s*.*?\*\*")
    matches = re.findall(pattern, Response)
    answers = [match for match in matches]
    return answers


def AccuracyRate(Answers:list, Questions:list)->float:
    # 正解率を計算する
    correct_count = 0
    for i, question in enumerate(Questions):
        if i >= len(Answers): # 回答が不足している場合
            break
        if question['Correct'] == Answers[i]:
            correct_count += 1
        else:
            print(f"Incorrect: {question['Q']}")
            print(f"Expected: {question['Correct']}, Got: {Answers[i]}")
    accuracy_rate = correct_count / len(Questions) * 100
    return accuracy_rate

if __name__ == "__main__":
    with open('/home/ryoma/nock100/S5LLM/japanese_history.csv') as file:
        lines = file.readlines()

    Questions = SplitQustion_Option(lines)
    prompt = CreatePrompt(Questions)
    # print(prompt) #Question_JapaseHistory.txt
    Response = FetchAnswer_gemini(prompt, MaxOutputTokens=2500)
    # print(Response) #Answer_JapaseHistory.txt
    Answers = ExtractAnswer(Response)
    AccuracyRate = AccuracyRate(Answers, Questions)
    print(f"Accuracy Rate: {AccuracyRate}%")

"""
Incorrect: 「三奉行の最高格は{ }である」の空欄に当てはまるものは？
Expected: D, Got: A
Incorrect: 「『養老律令』は，{ }天皇の治世に藤原不比等らによって編纂された」の空欄に当てはまるものは？
Expected: D, Got: A
Incorrect: 「1905年，{ }を締結し，韓国の外交権を奪って保護国化した」の空欄に当てはまるものは？
Expected: D, Got: A
Incorrect: 1956年に締結された日本とソ連との国交回復を果たした条約は何か
Expected: D, Got: A
Incorrect: 金輸出再禁止を行った大蔵大臣は誰か
Expected: D, Got: C
Incorrect: 第二次農地改革を始めた内閣の首相は誰か
Expected: C, Got: A
Incorrect: 1950年、レッド＝パージに供いない結成された、反共を方針とする労働組合の名前は
Expected: C, Got: A
Incorrect: 「縄文時代には{ }石器が使用された」の空欄に当てはまるものは？
Expected: A, Got: B
Incorrect: 日露和親条約で新たに開港されたのはどこか
Expected: B, Got: D
Incorrect: 日本最初の合法的な社会主義政党は何か
Expected: B, Got: A
Incorrect: 1898年に成立した日本初の政党内閣の名を答えよ
Expected: B, Got: A
Incorrect: 「佐賀県唐津市の{ }遺跡からは，縄文晩期の水田跡などが発見された」の空欄に当てはまるものは？
Expected: D, Got: A
Incorrect: 「徳川綱吉は，大老{ }の補佐で天和の治と呼ばれる文治政治を推進した」の空欄に当てはまるものは？
Expected: B, Got: A
Incorrect: 「江戸時代初期～前期の百姓一揆は，{ }一揆と呼ばれるものが多かった」の空欄に当てはまるものは？
Expected: D, Got: C
Incorrect: 1947年、傾斜生産方式を実施した時の首相は誰か
Expected: B, Got: A
Accuracy Rate: 90.0%
"""
