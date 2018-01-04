# http://d.hatena.ne.jp/jetbead/20110904/1315147133
def bi_gram(str_split):
    n_gram = []
    for i in range(0, len(str_split) - 1):
        n_gram.append(str_split[i:i + 2])
    return n_gram

str_split = "I am an NLPer".split()
print(bi_gram(str_split)) # 単語bi-gram
print(bi_gram(''.join(str_split))) # 文字bi-gram
