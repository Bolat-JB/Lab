import datetime

date1 = input("YYYY-MM-DD HH:MM:SS :")
date2 = input("YYYY-MM-DD HH:MM:SS :")

firstDate = datetime.datetime.strptime(date1, "%Y-%m-%d %H-%M-%S")
secondDate = datetime.datetime.strptime(date2, "%Y-%m-%d %H-%M-%S")
print(firstDate-secondDate)