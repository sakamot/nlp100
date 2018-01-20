file_list = open('hightemp.txt').readlines()
split_list = [ f.split('\t') for f in file_list ]
sort = {}
for s in split_list:
    if s[0] in sort:
        sort[s[0]] += 1
    else:
        sort[s[0]] = 1

for k, v in sorted(sort.items(), key=lambda x: -x[1]):
    print(str(v) + ' ' + str(k))
