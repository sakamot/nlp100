import re
from q20 import load_file

pattern = r"^\{\{基礎情報.*?$(.*?)^\}\}$"
repattern = re.compile(pattern, re.MULTILINE + re.VERBOSE + re.DOTALL)

match = repattern.findall(load_file())
pat = r"^\|(.+?) = (.+?)\n"
repat = re.compile(pat, re.MULTILINE + re.VERBOSE + re.DOTALL)
match1 = repat.findall(match[0])

dic = { m[0]: re.sub(r"'{3,5}", "", m[1]) for m in match1 }
print(dic)
