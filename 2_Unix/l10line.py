def count_line(path:str)->int:
    with open(path) as file:
        line_list = file.readlines()
        
    return len(line_list)


if __name__ == "__main__":
    lines = count_line("/home/ryoma/nock100/2_Unix/popular-names.txt")
    print("number of lines: ",lines)