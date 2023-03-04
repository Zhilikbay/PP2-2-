def f(a):
    return a == ''.join(reversed(a))
a=input()
if f(a):
    print("YES")
else:
    print("NO")