def extract_1357(sentence: str)->str:
    extract = sentence[0:8:2] #1文字目から1文字飛ばしで7文字目まで
    return extract

if __name__ == "__main__":
    extract = extract_1357("パタトクカシー")
    print(extract)