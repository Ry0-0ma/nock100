import sys

if __name__=="__main__":
    N = int(sys.argv[1]) #コマンドラインから末尾何行表示するか指定    
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()

    tail_N = ''.join(line_list[len(line_list)-N:len(line_list)])

    print(tail_N.strip()) #最終行の改行を削除
