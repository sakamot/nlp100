import re
from q20 import load_file

split_text = load_file().splitlines()
pattern = r"\[\[Category"
repattern = re.compile(pattern)

for t in split_text:
    if repattern.match(t):
        print(t)
