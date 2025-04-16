import sys

def split_lines(line_list:list, splited_count:list)->list:
    splited = []
    total_line = 0
    for line_count in splited_count:
        splited.append(''.join(line_list[total_line:total_line+line_count]))
        total_line += line_count #分割した行数の累積和

    return splited

def count_lines(line_list:list, N:int)->list:
    lines = len(line_list)//N #何行ずつ分割するのか
    splited_count = [lines]*N #分割されたtxtのそれぞれの行数
    for i in range(len(line_list) % N +1): #余りを分配
        splited_count[i] += 1

    return splited_count

def save_splited(splited:list, N:int):
    for i in range(N):
        with open("/home/ryoma/nock100/2_Unix/splited%s.txt" % str(i+1), mode='w') as file:
            file.write(''.join(splited[i]))

if __name__ == "__main__":
    N = int(sys.argv[1]) #コマンドラインから何分割するか指定
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()
    
    splited_count = count_lines(line_list, N) #分割されたtxtのそれぞれの行数の累積和を返す
    splited = split_lines(line_list, splited_count)
    save_splited(splited, N)

