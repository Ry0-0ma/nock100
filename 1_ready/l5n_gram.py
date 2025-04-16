def make_n_gram(sequence, n:int)->list:
    n_gram = []
    for i in range(len(sequence)-(n-1)): #先頭からn個ずつ追加
        if sequence[i:i+n] not in n_gram:
            n_gram.append(sequence[i:i+n])
    
    return n_gram


if __name__ == "__main__":
    sentence = 'I am an NLPer'
    char_bi_gram = make_n_gram(sentence, 2)

    words = sentence.split(' ')
    word_bi_gram = make_n_gram(words, 2)

    print('character bi-gram')
    print(char_bi_gram)

    print('word bi-gram')
    print(word_bi_gram)