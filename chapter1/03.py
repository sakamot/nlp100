str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
list = []
for s in str.split(' '):
    list.append(len(s.strip(',.')))
print(list)
