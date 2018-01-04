def bi_gram(str_split):
    n_gram = []
    for i in range(0, len(str_split) - 1):
        n_gram.append(str_split[i:i + 2])
    return n_gram

str1 = 'paraparaparadise'
str2 = 'paragraph'
print(bi_gram(str1))

x = set(bi_gram(str1))
y = set(bi_gram(str2))
print(x | y) # 和集合
print(x & y) # 積集合
print(x - y) # 差集合
print('se' in x | y)
