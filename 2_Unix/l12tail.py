import sys

if __name__=="__main__":
    N = int(sys.argv[1]) #コマンドラインから末尾何行表示するか指定    
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()

    tail_N = ''.join(line_list[len(line_list)-N:len(line_list)])

    print(tail_N.strip()) #最終行の改行を削除

"""
(myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ python l12tail.py 10
Liam    M       19837   2018
Noah    M       18267   2018
William M       14516   2018
James   M       13525   2018
Oliver  M       13389   2018
Benjamin        M       13381   2018
Elijah  M       12886   2018
Lucas   M       12585   2018
Mason   M       12435   2018
Logan   M       12352   2018
"""
"""
(myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ tail -n 10 popular-names.txt
Liam    M       19837   2018
Noah    M       18267   2018
William M       14516   2018
James   M       13525   2018
Oliver  M       13389   2018
Benjamin        M       13381   2018
Elijah  M       12886   2018
Lucas   M       12585   2018
Mason   M       12435   2018
Logan   M       12352   2018
"""

