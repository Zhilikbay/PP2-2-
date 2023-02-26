import datetime

cur = datetime.date.today()
sub = datetime.timedelta(days=5)
ne = cur-sub
print(cur.strftime("%A"))
print(ne.strftime("%A"))

