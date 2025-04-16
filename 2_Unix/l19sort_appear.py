from l12save_column import save_column

def count_appear(col_list:list)->list:
    appear_count = []
    for word in col_list:
        appear_count.append(col_list.count(word)) #出現回数
    
    # print(type(appear_count[2]))
    return appear_count


def sort_appear(appear_count:list, line_list:list)->list:
    appear_dict = dict(zip(line_list, appear_count))
    
    sorted_appear = sorted(appear_dict.items(), key=lambda x:x[1], reverse=True)

    return dict(sorted_appear).keys()


if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/col1.txt") as file:
        col_list = file.readlines()
    
    appear_count = count_appear(col_list)

    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()

    sorted_appear = sort_appear(appear_count, line_list)
    save_column(''.join(sorted_appear), "/home/ryoma/nock100/2_Unix/sort_appear.txt")

# 結果の一部は、名前が混ざっていたりする->出現回数が同じ名前