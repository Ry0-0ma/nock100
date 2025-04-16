def fusion(sentence1: str, sentence2: str)->str: #同じ長さの単語
    fused = []
    for i in range(len(sentence1)):
        fused.append(sentence1[i])
        fused.append(sentence2[i])
    
    return fused



if __name__ == "__main__":
    fused = fusion("パトカー", "タクシー")
    print(''.join(fused)) #リストをstrに変換
    print(type(''.join(fused)))