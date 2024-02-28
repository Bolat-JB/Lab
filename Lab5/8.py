import re

with open('row.txt','r', encoding='utf-8') as t:
    txt = t.read()

def splitup(s):
    return re.findall('[A-Z][^A-Z]*', s)

result = splitup(txt)

print(result)
