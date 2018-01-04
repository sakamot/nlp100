# 08
def cipher(string):
    text = ''
    for c in string:
        if c.islower():
            text += (chr(219 - ord(c)))
        else:
            text += (c)
    return text

str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."
print(str)
print(cipher(str))
print(cipher(cipher(str)))
