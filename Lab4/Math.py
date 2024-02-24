import math

# ex1
d = int(input("Input degree: "))
print("Output radian:", math.radians(d))

# ex2
h = int(input("Height: "))
a = int(input("Base, first value: "))
b = int(input("Base, second value: "))

print("Expected output:", (a+b)*h/2)

# ex3
import math

n = int(input("Number of sides: "))
l = int(input("Length of the side: "))

area = (l**2*n)/(math.tan(math.pi/n)*4)
print("The area of the polygon is:", int(area))


# ex4
l = int(input("Length of base: "))
h = int(input("Height of parallelogram: "))

print("Expected output: ", float(l*h))