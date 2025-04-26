# ライブラリに親しむ

import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

def CountToken_gemini(
        prompt:str, 
        model:str='gemini-2.0-flash',   #公式デフォルトパラメータ
        MaxOutputTokens:int=1024,       #2048トークン
        Temperature:float=0.1,          #0.1
        TopP:float=0.95,                #0.95
        TopK:int=32                     #32
    ):
    # .envファイルからAPIキーを読み込む
    load_dotenv()
    API_KEY = os.getenv('GOOGLE_GEMINI_API_KEY')
    # genai.configure(api_key=API_KEY)
    client = genai.Client(api_key=API_KEY)
    # gemini = genai.GenerativeModel(model)
    NumToken = client.models.count_tokens(
        model=model, contents=prompt
    )
    print(f"トークン数: {NumToken}")
    answer = client.models.generate_content(
        model=model, contents=prompt,
        config=types.GenerateContentConfig(
            max_output_tokens=MaxOutputTokens,
            temperature=Temperature,
            top_p=TopP,
            top_k=TopK,
        )
    )
    print(answer.usage_metadata)
    print(answer.text)
    # answer = gemini.generate_content(question)

if __name__ == "__main__":
    prompt = """
吾輩は猫である。名前はまだ無い。

どこで生れたかとんと見当がつかぬ。何でも薄暗いじめじめした所でニャーニャー泣いていた事だけは記憶している。吾輩はここで始めて人間というものを見た。しかもあとで聞くとそれは書生という人間中で一番獰悪な種族であったそうだ。この書生というのは時々我々を捕えて煮て食うという話である。しかしその当時は何という考もなかったから別段恐しいとも思わなかった。ただ彼の掌に載せられてスーと持ち上げられた時何だかフワフワした感じがあったばかりである。掌の上で少し落ちついて書生の顔を見たのがいわゆる人間というものの見始であろう。この時妙なものだと思った感じが今でも残っている。第一毛をもって装飾されべきはずの顔がつるつるしてまるで薬缶だ。その後猫にもだいぶ逢ったがこんな片輪には一度も出会わした事がない。のみならず顔の真中があまりに突起している。そうしてその穴の中から時々ぷうぷうと煙を吹く。どうも咽せぽくて実に弱った。これが人間の飲む煙草というものである事はようやくこの頃知った。
"""
    CountToken_gemini(prompt)

    """
    トークン数: total_tokens=272 cached_content_token_count=None
cache_tokens_details=None cached_content_token_count=None candidates_token_count=157 candidates_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=157)] prompt_token_count=252 prompt_tokens_details=[ModalityTokenCount(modality=<MediaModality.TEXT: 'TEXT'>, token_count=252)] thoughts_token_count=None tool_use_prompt_token_count=None tool_use_prompt_tokens_details=None total_token_count=409 traffic_type=None
はい、これは夏目漱石の小説『吾輩は猫である』の冒頭部分ですね。猫の視点から人間社会を観察するという斬新なスタイルで、ユーモラスかつ辛辣な風刺が込められています。

この部分を読んで感じたことや、何か質問があれば教えてください。例えば、以下のようなことが考えられます。

*   **猫の視点:** なぜ作者は猫を語り手に選んだのか？
*   **書生:** 書生はどのような人物として描かれているのか？
*   **ユーモア:** どのような表現にユーモアを感じるか？
*   **風刺:** この部分にはどのような風刺が込められているか？

どんなことでも構いませんので、お気軽にお尋ねください。
    """