import sys


if __name__ == "__main__":
    N = int(sys.argv[1]) #コマンドラインから先頭何行表示するか指定
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()

    head_N = ''.join(line_list[0:N])
    
    print(head_N.rstrip()) #最終行の改行を削除
    