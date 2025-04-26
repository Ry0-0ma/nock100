# 汎用コードをつくる
# 誤解のない名前

import os
from dotenv import load_dotenv
# import google.generativeai as genai
from google import genai
from google.genai import types

# APIリクエストを送信して解答を取得する関数
def FetchAnswer_gemini(
        prompt:str, 
        model:str='gemini-2.0-flash',   #公式デフォルトパラメータ
        MaxOutputTokens:int=1024,       #2048トークン
        Temperature:float=0.1,          #0.1
        TopP:float=0.95,                #0.95
        TopK:int=32                     #32
    ) -> str:
    # .envファイルからAPIキーを読み込む
    load_dotenv()
    API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')
    # genai.configure(api_key=API_KEY)
    client = genai.Client(api_key=API_KEY)
    # gemini = genai.GenerativeModel(model)
    answer = client.models.generate_content(
        model=model, contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=MaxOutputTokens,
            temperature=Temperature,
            top_p=TopP,
            top_k=TopK,
        )
    )

    # answer = gemini.generate_content(question)
    return answer.text
   

if __name__ == "__main__":
    question = """
9世紀に活躍した人物に関係するできごとについて述べた次のア～ウを年代の古い順に正しく並べよ。

ア 藤原時平は，策謀を用いて菅原道真を政界から追放した。
イ 嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。
ウ 藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。
"""
    # 解答を取得
    answer = FetchAnswer_gemini(question)
    print(answer)
"""(パラメータ設定前)
年代の古い順に並べると以下のようになります。

1.  **イ 嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。**
    *   嵯峨天皇の在位は809年～823年であり、この頃に藤原冬嗣が蔵人頭に任命されたと考えられます。

2.  **ウ 藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。**
    *   承和の変は842年に起こりました。藤原良房はこの変に乗じて勢力を拡大しました。

3.  **ア 藤原時平は，策謀を用いて菅原道真を政界から追放した。**
    *   菅原道真が太宰府に左遷されたのは901年です。藤原時平が道真を追放したのはこの頃です。

したがって、正解は **イ → ウ → ア** となります。
"""    
"""'(パラメータ設定後)
年代の古い順に並べると以下のようになります。

1.  **イ 嵯峨天皇は，藤原冬嗣らを蔵人頭に任命した。** (810年)
2.  **ウ 藤原良房は，承和の変後，藤原氏の中での北家の優位を確立した。** (842年)
3.  **ア 藤原時平は，策謀を用いて菅原道真を政界から追放した。** (901年)

したがって、正解は **イ → ウ → ア** です。
"""

"""
パラメータ
stopSequences: 出力を停止する文字シーケンス
temperature: 出力のランダム性[0.0~2.0]
maxOutputTokens: 出力トークン数の上限
topP: 確率の合計がtopPと等しくなるまで確率の高いものから低いものへ: デフォ0.95
topK: 確率の高いものからtopK個を選択する
"""


"""
モデルバージョン https://ai.google.dev/gemini-api/docs/rate-limits
モデル名	    リクエスト数/分     トークン数/分   リクエスト数/日
gemini-2.0-flash	15              1,000,000	    1,500
gemini-1.5-pro	    2	            32,000	        50
gemini-2.5-pro-preview-03-25
"""

