def squares(a, b):
    for i in range(a, b+1):
        yield i**2



for j in squares(1,5):
    print(j)
