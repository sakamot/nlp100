print('自然数を入力')
input_num = int(input())

file_list = open('hightemp.txt').readlines()
for line in file_list[len(file_list)- input_num:]:
    print(line, end='')
