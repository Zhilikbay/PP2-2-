import re

def f(s):
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()
a=input()
print(f(a))
