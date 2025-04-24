# 名前
import random
from l14save_column import save_column

def shuffle_lines(line_list:list)->list:
    random_idx = random.sample(range(len(line_list)), len(line_list))
    shuffled_lines = []
    for i in random_idx:
        shuffled_lines.append(line_list[i])
    return shuffled_lines

if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()
    
    MyShuffled = shuffle_lines(line_list) #中身を変えずにシャッフル
    random.shuffle(line_list) #直接中身をシャッフル
    save_column(''.join(MyShuffled), "/home/ryoma/nock100/2_Unix/MyShuffled.txt")
    save_column(''.join(line_list), "/home/ryoma/nock100/2_Unix/Shuffled.txt")

"""
Isabella	F	14464	2018
Joseph	M	25699	1922
James	M	42118	1918
Daniel	M	35001	1989
Sophia	F	14883	2017
Mary	F	45345	1914
William	M	20225	2004
Robert	M	61669	1927
Dorothy	F	7318	1910
Karen	F	32872	1965
Abigail	F	12409	2013
.
.
.
"""