import re

with open('row.txt','r',encoding='utf-8') as k:
    txt = k.read()

x = re.search("a.*b", txt)
print(x)