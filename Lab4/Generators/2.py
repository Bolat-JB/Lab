def even(n):
    for i in range(n+1):
        if i%2==0:
            yield i

a = int(input())
b = even(a)

c = ', '.join(map(str, b))
print(c)