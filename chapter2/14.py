print('自然数を入力')
input_num = int(input())

file_list = open('hightemp.txt').readlines()
for line in file_list[0:input_num]:
    print(line, end='')
