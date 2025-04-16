def tab_to_space(line:str)->str:
    words = line.split("\t")
    
    return ' '.join(words)



if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/popular-names.txt") as file:
        line_list = file.readlines()
    
    space_line = tab_to_space(line_list[0])
    print(line_list[0])
    print(space_line)