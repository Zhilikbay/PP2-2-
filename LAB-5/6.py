import re

def f(s):
    return re.sub(r'[ ,.]', ':', s)

a=input()
print(f(a))
