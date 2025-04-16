# 同様
def Extract2468(sentence: str)->str:
    extract = sentence[1::2] #1文字目から1文字飛ばしで8文字目まで
    return extract

if __name__ == "__main__":
    extract = Extract2468("パタトクカシーー")
    print(extract)