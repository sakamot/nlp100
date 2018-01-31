import re
from q20 import load_file

split_text = load_file().splitlines()
pattern = r"\[\[File:(.*?)\|thumb"
repattern = re.compile(pattern)

for t in split_text:
    match = repattern.match(t)
    if match:
        print(match[1])
