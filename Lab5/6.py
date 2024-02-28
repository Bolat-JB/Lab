with open('row.txt', 'r', encoding='utf-8') as t:
    txt = t.read()

mdi = txt.replace(' ',':').replace('.',':').replace(',',':')
print(mdi)