import math

print('自然数を入力')
input_num = int(input())

file_list = open('hightemp.txt').readlines()
file_size = math.ceil(len(file_list) / input_num)
for n in range(0, file_size):
    f = open(str(n+1)+'.txt', 'w')
    f.write(''.join(file_list[n*input_num:(n+1)*input_num:1]))
    f.close()
