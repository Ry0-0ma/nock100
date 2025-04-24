# 無関係の下位問題を抽出する
from l14save_column import save_column

def count_appear(col_list:list)->list:
    appear_count = []
    for word in col_list:
        appear_count.append(col_list.count(word)) #出現回数(重複した回数)
    # print(type(appear_count[2]))
    return appear_count


def sort_appear(appear_count:list, line_list:list)->list:
    appear_dict = dict(zip(line_list, appear_count))
    # その名前の出現数でソート
    sorted_appear = sorted(appear_dict.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_appear).keys()


def SortAppear_eachName(appear_count:int, col_list:list)->list:
    appear_dict = dict(zip(col_list, appear_count))
    # その名前の出現数でソート
    sorted_appear = sorted(appear_dict.items(), key=lambda x:x[1], reverse=True)
    return sorted_appear

def PrintSortAppear(sorted_appear:dict):
    for name, count in sorted_appear:
        print(f"{name.strip()}: {count}") #空白削除しながら出力
    

if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/col1.txt") as file: #1列目(名前)のファイルを参照
        col_list = file.readlines()
    
    appear_count = count_appear(col_list)
    sort_appear = SortAppear_eachName(appear_count, col_list)
    PrintSortAppear(sort_appear)

"""
# 2020 版でつかった
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()
    sorted_appear = sort_appear(appear_count, line_list)
    save_column(''.join(sorted_appear), "/home/ryoma/nock100/2_Unix/sort_appear.txt")
# 結果の一部は、名前が混ざっていたりする->出現回数が同じ名前
"""

# cut -f 1 popular-names.txt | sort | uniq -c | sort -nr > Unix_sort_appear.txt

"""
James: 118
William: 111
John: 108
Robert: 108
Mary: 92
Charles: 75
Michael: 74
Elizabeth: 73
Joseph: 70
Margaret: 60
George: 58
Thomas: 58
David: 57
Richard: 51
Helen: 45
Frank: 43
Christopher: 43
Anna: 41
Edward: 40
Ruth: 39
Patricia: 38
Matthew: 37
Dorothy: 36
Emma: 35
Barbara: 32
Daniel: 31
Joshua: 31
Sarah: 26
Linda: 26
Jennifer: 26
Emily: 26
Jessica: 25
Jacob: 25
Mildred: 24
Betty: 24
Susan: 24
Henry: 23
Ashley: 23
Nancy: 22
Andrew: 21
Florence: 20
Marie: 20
Donald: 20
Amanda: 20
Samantha: 19
Karen: 18
Lisa: 18
Melissa: 18
Madison: 18
Olivia: 18
Stephanie: 17
Abigail: 17
Ethel: 16
Sandra: 16
Mark: 16
Frances: 15
Carol: 15
Angela: 15
Michelle: 15
Heather: 15
Ethan: 15
Isabella: 15
Shirley: 14
Kimberly: 14
Amy: 14
Ava: 14
Virginia: 13
Deborah: 13
Brian: 13
Jason: 13
Nicole: 13
Hannah: 13
Sophia: 13
Minnie: 12
Bertha: 12
Donna: 12
Cynthia: 11
Alice: 10
Doris: 10
Ronald: 10
Brittany: 10
Nicholas: 10
Mia: 10
Noah: 10
Joan: 9
Debra: 9
Tyler: 9
Ida: 8
Clara: 8
Judith: 8
Taylor: 8
Alexis: 8
Alexander: 8
Mason: 8
Harry: 7
Sharon: 7
Steven: 7
Tammy: 7
Brandon: 7
Liam: 7
Anthony: 6
Annie: 5
Gary: 5
Jeffrey: 5
Jayden: 5
Charlotte: 5
Lillian: 4
Kathleen: 4
Justin: 4
Austin: 4
Chloe: 4
Benjamin: 4
Evelyn: 3
Megan: 3
Aiden: 3
Harper: 3
Elijah: 3
Bessie: 2
Larry: 2
Rebecca: 2
Lauren: 2
Amelia: 2
Oliver: 2
Walter: 1
Carolyn: 1
Pamela: 1
Lori: 1
Laura: 1
Tracy: 1
Julie: 1
Scott: 1
Kelly: 1
Crystal: 1
Rachel: 1
Logan: 1
Lucas: 1
Logan: 1
"""