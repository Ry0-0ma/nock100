#ライブラリに親しむ
def count_line(path:str)->int:
    with open(path) as file:
        line_list = file.readlines()
        
    return len(line_list)


if __name__ == "__main__":
    lines = count_line("/home/ryoma/nock100/2_Unix/popular-names.txt")
    print("number of lines: ",lines)

    """
    (myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ python l10line.py
    number of lines:  2780
    """
    """
    (myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ wc -l popular-names.txt
    2780 popular-names.txt
    """
