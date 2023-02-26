def q(N):
    for i in range(1,N+1):
        yield i**2
N=5
for j in q(N):
    print(j)
    