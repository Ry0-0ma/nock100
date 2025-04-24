from l14save_column import save_column

def merge_column(col1:list, col2:list)->str:
    merged = []
    for i in range(len(col1)):
        word1 = col1[i].rstrip() #\n を削除
        word2 = col2[i]
        line = [word1, word2]
        merged.append("\t".join(line))

    return "\n".join(merged)


if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/col1.txt") as file:
        col1 = file.readlines()
    
    with open("/home/ryoma/nock100/2_Unix/col2.txt") as file:
        col2 = file.readlines()
    
    merged = merge_column(col1, col2)
    save_column(merged, "/home/ryoma/nock100/2_Unix/merged.txt")

