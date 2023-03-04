from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10]
b=reduce(lambda x,y:x*y,a)
print(b)