file = open('hightemp.txt')
for line in file:
    print(line.replace('\t', ' '), end='')
