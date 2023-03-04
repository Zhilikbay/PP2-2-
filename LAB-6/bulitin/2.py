string=input()
a=sum(1 for c in string if c.isupper())
b=sum(1 for c in string if c.islower())
print(a,b)