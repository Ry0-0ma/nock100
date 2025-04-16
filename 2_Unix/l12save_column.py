def extract_column(line_list:list, num_col:int)->str:
    column_list = []
    for line in line_list:
        words = line.split("\t")
        column_list.append(words[num_col-1])
    
    return "\n".join(column_list)

def save_column(column:str, path:str):
    with open(path, mode='w') as file:
        file.write(column)
    


if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()
    
    column1 = extract_column(line_list, 1) #1列目
    save_column(column1, "/home/ryoma/nock100/2_Unix/col1.txt")
    
    column2 = extract_column(line_list, 2) #2列目
    save_column(column2, "/home/ryoma/nock100/2_Unix/col2.txt")

        