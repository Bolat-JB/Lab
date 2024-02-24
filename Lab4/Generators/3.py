def div(n):
    for i in range(1, n+1):
        if i%3==0 and i%4==0:
            yield i
            
num = int(input())
a = div(num)
for i in a:
    print(i)