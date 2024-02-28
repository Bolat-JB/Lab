import re

with open('row.txt', 'r', encoding='utf-8') as f:
    txt = f.read()

x = re.findall('[a-z]+_[a-z]', txt)

for sequence in x:
    print(sequence)