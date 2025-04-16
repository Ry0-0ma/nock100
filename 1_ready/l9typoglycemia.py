# 10章: 無関係な下位問題を抽出
import random

#先頭と末尾以外の順序をランダムに並び変える
def shuffle_word(word:list)->str:
    shuffled = [word[0]]
    end = len(word)-1
    middle = word[1:end]
    shuffled.append(''.join(random.sample(middle, len(middle))))
    shuffled.append(word[end])
    print(shuffled)
    return ''.join(shuffled)

# 先頭と末尾以外がバラバラな単語の文を生成
def typoglysemia(word_list:list)->str:
    shuffle_list = []
    for word in word_list:
        if len(word) <= 4:
            shuffle_list.append(word)
        else:
            shuffle_list.append(shuffle_word(word))
    
    return ' '.join(shuffle_list)

if __name__ == "__main__":
    sentence = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
    words = sentence.split(' ')

    shuffled = typoglysemia(words)
    print(shuffled)