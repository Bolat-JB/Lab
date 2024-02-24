# ex1
def square(N):
    f = 1
    while f<=N:
        yield f*f
        f+=1

a = int(input())

b = square(a)
for i in b:
    print(i)
    
    
# ex2
def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

a = int(input())
b = even(a)

c = ', '.join(map(str, b))
print(c)


# ex3
def div(n):
    for i in range(1, n+1):
        if i%3==0 and i%4==0:
            yield i
            
num = int(input())
a = div(num)
for i in a:
    print(i)
    
    
# ex4
def squares(a, b):
    for i in range(a, b+1):
        yield i**2
        
a = int(input())
b = int(input())
square = squares(a, b)

for i in square:
    print(i)
    
    
# ex5
def o(n):
    for i in range(n+1):
        yield n-i
        
a = int(input())
b = o(a)
for i in b:
    print(i)