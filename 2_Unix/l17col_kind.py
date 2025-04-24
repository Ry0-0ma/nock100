from l14save_column import save_column

def col_kind(col_list:list)->list:
    kinds = []
    for word in col_list:
        if word not in kinds:
            kinds.append(word)
    
    return kinds

if __name__ == "__main__":
    with open("/home/ryoma/nock100/2_Unix/col1.txt") as file:
        col_list = file.readlines()
    
    kinds = col_kind(col_list)
    kinds = ''.join(sorted(kinds))

    save_column(kinds, "/home/ryoma/nock100/2_Unix/kinds.txt")

"""
cut -f 1 popular-names.txt | sort | uniq > Unix_kinds.txt
Abigail
Aiden
Alexander
Alexis
Alice
Amanda
Amelia
Amy
Andrew
Angela
Anna
Annie
Anthony
Ashley
Austin
.
.
.
Virginia
Walter
William
"""
    