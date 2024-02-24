import datetime
x = datetime.datetime.now()
y = x - datetime.timedelta(days=1)
t = x + datetime.timedelta(days=1)
print("Yesterday:", y.strftime("%d"))
print("Today:", x.strftime("%d"))
print("Tomorrow:", t.strftime("%d"))
