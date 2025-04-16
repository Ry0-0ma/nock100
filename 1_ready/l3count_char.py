# 11章1度に一つのことを
# p.135 10章汎用コードをつくる
import numpy as np

def Count_char(words:list)->np.ndarray:
    word_count = len(words)
    counts = np.zeros(word_count)
    for i in range(word_count):
        counts[i] = len(words[i])

    return counts

def remove_stopword(sentence:str)->str:
    sentence = sentence.replace(',','')
    sentence = sentence.replace('.','')

    return sentence

if __name__ == "__main__":
    sentence = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
    sentence = remove_stopword(sentence)
    words = sentence.split(' ') #空白ごとに格納
    
    counts = Count_char(words)
    print(counts)
    