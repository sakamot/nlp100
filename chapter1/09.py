import random

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

random_arry = []
for s in str.split():
    if len(s) > 4:
        list_s = list(s)[1:len(s)-1]
        random.shuffle(list_s)
        text = s[0] + ''.join(list_s) + s[len(s)-1]
        random_arry.append(text)
    else:
        random_arry.append(s)

print(' '.join(random_arry))
