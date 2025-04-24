# 汎用コードをつくる

from l14save_column import save_column
import numpy as np

def extract_column_np(line_list:list, num_col:int)->np.ndarray:
    column_list = []
    for line in line_list:
        words = line.split("\t")
        column_list.append(int(words[num_col-1]))  #数値を追加
    
    return np.array(column_list)

def sort_by_column(dictionary:dict)->str:
    sorted_dict = sorted(dictionary.items(), key=lambda x:x[0], reverse=True) #list型
    sorted_lines = dict(sorted_dict).values() #dict_kyes型

    return ''.join(sorted_lines)    

if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()

    # extract_column は最後strにして返すので、行ごとのリストにならない
    column3 = extract_column_np(line_list,3) #3列目
    # save_column(column3, "/home/ryoma/nock100/2_Unix/col3.txt")
    dictionary = dict(zip(column3, line_list)) #3列目をkey にして
    # print(type(column3[0]))
    # print(sorted(column3))
    
    sorted_lines = sort_by_column(dictionary)
    save_column(sorted_lines, "/home/ryoma/nock100/2_Unix/sorted_lines.txt")



