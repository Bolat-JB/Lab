with open('row.txt', 'r', encoding='utf-8') as t:
    txt = t.read()
tx = txt.split('_')
wor = tx[0] + ''.join(w.capitalize() for w in tx[1:])

print(wor)