file = open('hightemp.txt')
col1 = open('col1.txt', 'w')
col2 = open('col2.txt', 'w')
for line in file:
    line_list = line.split('\t')
    col1.write(line_list[0])
    col1.write('\n')
    col2.write(line_list[1])
    col2.write('\n')
