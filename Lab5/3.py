import re

with open('row.txt','r',encoding='utf-8') as t:
    txt = t.read()
    
x = re.findall(r'\b[A-Z]+_[a-z]\b+',txt)
print()