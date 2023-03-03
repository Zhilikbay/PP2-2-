import re
def space(s):
    return re.sub(r"(\w)([A-Z])", r"\1 \2", s)

a=input()
print(space(a))  
