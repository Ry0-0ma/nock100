def Encrypt(sentence:str)->str:
    cipher = []
    for char in sentence:
        if char.islower(): #英小文字
            cipher.append(chr(219 - ord(char)))
        else:
            cipher.append(char)
    
    return ''.join(cipher)


if __name__ == "__main__":
    cipher = Encrypt('abc')
    print(cipher)
