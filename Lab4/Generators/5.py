def o(n):
    for i in range(n+1):
        yield n-i
        
a = int(input())
b = o(a)
for i in b:
    print(i)