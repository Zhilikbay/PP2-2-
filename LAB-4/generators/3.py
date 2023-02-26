def dev(n):
    for i in range(n+1):
        if i % 3 == 0 and i % 4 == 0:
            yield i

n = 36

for j in dev(n):
    print(j)