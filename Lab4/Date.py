import datetime

# ex1
x = datetime.datetime.now()
tom = x - datetime.timedelta(days=5)
print(tom)

# ex2
x = datetime.datetime.now()
y = x - datetime.timedelta(days=1)
t = x + datetime.timedelta(days=1)
print("Yesterday:", y.strftime("%d"))
print("Today:", x.strftime("%d"))
print("Tomorrow:", t.strftime("%d"))

# ex3
x = datetime.datetime.now().replace(microsecond=0)
print(x)

# ex4
date1 = input("YYYY-MM-DD HH:MM:SS :")
date2 = input("YYYY-MM-DD HH:MM:SS :")

firstDate = datetime.datetime.strptime(date1, "%Y-%m-%d %H-%M-%S")
secondDate = datetime.datetime.strptime(date2, "%Y-%m-%d %H-%M-%S")
print(firstDate-secondDate)