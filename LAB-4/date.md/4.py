import datetime


d1 = datetime.datetime(2022, 3, 1, 12, 0, 0)
d2 = datetime.datetime(2022, 3, 1, 13, 0, 0)


d_d = (d2 - d1).total_seconds()

print( d_d)