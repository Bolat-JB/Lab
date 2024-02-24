import math

n = int(input("Number of sides: "))
l = int(input("Length of the side: "))

area = (l**2*n)/(math.tan(math.pi/n)*4)
print("The area of the polygon is:", int(area))