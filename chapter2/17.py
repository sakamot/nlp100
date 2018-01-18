file_list = open('hightemp.txt').readlines()
row1 = []
for f in file_list:
    row1.append(f.split('\t')[0])

print('\n'.join(list(set(row1))))
