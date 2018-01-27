import re
from q20 import load_file

split_text = load_file().splitlines()
pattern = r"\[\[Category:(?P<name>.*)\]\]"
repattern = re.compile(pattern)

for t in split_text:
    match = repattern.match(t)
    if match:
        print(match.group('name'))
