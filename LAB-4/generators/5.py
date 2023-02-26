def down(n):
    while n >= 0:
        yield n
        n -= 1


for i in down(10):
    print(i)