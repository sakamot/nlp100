str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
dict = {}
for i, s in enumerate(str.split()):
    if i + 1 in [1, 5, 6, 7, 8, 9, 15, 16, 19]:
        dict[i] = s[0] # 1文字目
    else:
        dict[i] = s[0:2] # 0文字目から2文字
print(dict)
