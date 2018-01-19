file_list = open('hightemp.txt').readlines()
split_list = [ f.split('\t') for f in file_list ]
split_list.sort(key=lambda x:x[2], reverse=True)
for list in split_list:
    print('\t'.join(list), end='')
