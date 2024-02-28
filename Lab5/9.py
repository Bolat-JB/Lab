import re

def spaces(s):
    t = re.sub(r'([A-Z]+)', r' \1', s)
    return t
  
txt = "TheRainInSpain"
print(spaces(txt))
