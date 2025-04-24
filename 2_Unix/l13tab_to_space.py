# ライブラリに親しむ
def tab_to_space(line:str)->str: #タブをスペースに変換
    words = line.split("\t")
    
    return ' '.join(words)

def Printlist_tab_space(line_list:list, TopNum:int)->None:
    for i, line in enumerate(line_list):
        if i >= TopNum:
            break
        print(tab_to_space(line))

if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()
    
    Printlist_tab_space(line_list, 10)
    # for i in range(10):
    #     print(line_list[i])

    """
    (myenv3120) ryoma@DESKTOP-R18EQ88:~/nock100/2_Unix$ python l13tab_to_space.py
    Mary F 7065 1880

    Anna F 2604 1880

    Emma F 2003 1880

    Elizabeth F 1939 1880

    Minnie F 1746 1880

    Margaret F 1578 1880

    Ida F 1472 1880

    Alice F 1414 1880

    Bertha F 1320 1880

    Sarah F 1288 1880
    """

    """
    sed 's/\t/ /g' popular-names.txt | head -n 10   #s/\t/ /g: タブ文字 (\t) をスペースに置き換える。

    cat popular-names.txt | tr '\t' ' ' | head -n 10   #tr '\t' ' ': タブ文字をスペースに置き換える。

    expand -t 1 popular-names.txt | head -n 10   #-t 1: タブを1つのスペースに変換。

    Mary F 7065 1880
    Anna F 2604 1880
    Emma F 2003 1880
    Elizabeth F 1939 1880
    Minnie F 1746 1880
    Margaret F 1578 1880
    Ida F 1472 1880
    Alice F 1414 1880
    Bertha F 1320 1880
    Sarah F 1288 1880
    """

