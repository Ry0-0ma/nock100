# p.60 自分の考えを記録する
# HACK: 名前がビミョー
def generate_sentence(x:str, y:str, z:str)->str:
    sentence = [x,'時の',y,'は',z]
    return ''.join(sentence)


if __name__ == "__main__":
    sentence = generate_sentence('12', '気温', '22.4')
    print(sentence)