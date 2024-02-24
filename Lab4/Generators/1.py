def square(N):
    f = 1
    while f<=N:
        yield f*f
        f+=1

a = int(input())

b = square(a)
for i in b:
    print(i)