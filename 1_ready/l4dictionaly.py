from l3count_char import remove_stopword
import numpy as np

def extract_char(words:list)->list:
    first = np.array([1,5,6,7,8,9,15,16,19])
    extracted = []
    for i in range(len(words)):
        if i+1 in first:
            extracted.append(words[i][0])
        else:
            extracted.append(words[i][0:2])
    
    return extracted

def make_dictionary(words:list):
    index = [i+1 for i in range(len(words))]
    dictionary = dict(zip(index, words))
    sorted_dictionary = sorted(dictionary.items(), key=lambda x:x[1]) #値でアルファベット順にソート

    return sorted_dictionary    


if __name__ == "__main__":
    sentence = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
    sentence = remove_stopword(sentence)
    
    words = sentence.split(' ')
    words = extract_char(words)

    dictionary = make_dictionary(words)
    print(dictionary)
