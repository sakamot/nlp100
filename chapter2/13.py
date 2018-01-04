col1 = open('col1.txt').readlines()
col2 = open('col2.txt').readlines()
for (line1, line2) in zip(col1, col2):
    print(line1.replace('\n', '\t') + line2.rstrip('\n'))
