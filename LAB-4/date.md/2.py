import datetime

cur = datetime.date.today()
yest = datetime.timedelta(days=-1)
today = datetime.timedelta(days=1)
y=cur-yest
to=cur-today


print(to.strftime("%A"))
print(y.strftime("%A"))
print(cur.strftime("%A"))



