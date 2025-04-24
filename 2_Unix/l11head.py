import sys

if __name__ == "__main__":
    N = int(sys.argv[1]) #コマンドラインから先頭何行表示するか指定
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()

    head_N = ''.join(line_list[0:N])
    
    print(head_N.rstrip()) #最終行の改行を削除
    

    """
   (myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ python l11head.py 10
    Mary    F       7065    1880
    Anna    F       2604    1880
    Emma    F       2003    1880
    Elizabeth       F       1939    1880
    Minnie  F       1746    1880
    Margaret        F       1578    1880
    Ida     F       1472    1880
    Alice   F       1414    1880
    Bertha  F       1320    1880
    Sarah   F       1288    1880
    """

    """
    (myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ head -n 10 popular-names.txt
    Mary    F       7065    1880
    Anna    F       2604    1880
    Emma    F       2003    1880
    Elizabeth       F       1939    1880
    Minnie  F       1746    1880
    Margaret        F       1578    1880
    Ida     F       1472    1880
    Alice   F       1414    1880
    Bertha  F       1320    1880
    Sarah   F       1288    1880
    """