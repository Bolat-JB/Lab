import re

with open('row.txt','r', encoding='utf-8') as t:
    txt = t.read()

x = re.search("a.+b", txt)
print(x)