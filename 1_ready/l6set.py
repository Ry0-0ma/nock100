from l5n_gram import make_n_gram

def union(X:list, Y:list)->list:
    uni_set = X[:]
    for i in range(len(Y)):
        if Y[i] not in X:
            uni_set.append(Y[i])
            
    return uni_set

def intersection(X:list, Y:list)->list:
    inter_set = []
    for i in range(len(X)):
        if X[i] in Y:
            inter_set.append(X[i])
    
    return inter_set

def difference(X:list, Y:list)->list:
    dif_set = X[:]
    inter_set = intersection(X, Y)
    for i in range(len(inter_set)):
        dif_set.remove(inter_set[i])

    return dif_set        

def print_include(sets:list, char:str):
    print(sets)
    if char in sets:
        print("Including", char)
    else:
        print("Not including", char)

if __name__ == "__main__":
    #文字bi-gram を生成
    X = make_n_gram('paraparaparadise', 2)
    Y = make_n_gram('paragraph', 2)

    uni_set = union(X, Y)
    inter_set = intersection(X, Y)
    dif_set = difference(X, Y)

    print('Union:', uni_set)

    print('Intersection:', inter_set)

    print('Difference:', dif_set)

    print_include(X, 'se')
    print_include(Y, 'se')

    print()
    #list型ではなく、set型を使って
    X_set = set(X)
    Y_set = set(Y)

    print('Union:', X_set | Y_set)
    
    print('Intersection:', X_set.intersection(Y_set))

    print('Difference: ', X_set - Y_set)

    
    
    

