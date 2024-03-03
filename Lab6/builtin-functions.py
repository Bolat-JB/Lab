# ex1
a = list(input().split())
multiple = 1
for i in a:
    multiple*=int(i)
print(multiple)

# ex2
s = input()
up = "QWERTYUIOPASDFGHJKLZXCVBNM"
low = "wqertyuiopasdfghjklzxcvbnm"
upn = 0
lown = 0

for i in s:
    for j in up:
        if i==j:
            upn+=1
    for k in low:
        if i==k:
            lown+=1
            
print("Upper case:", upn)
print("Lower case:", lown)

# ex3
s = input()
j=int(len(s))-1
pol = True
for i in range(0, int(len(s)/2)):
    if s[i]!=s[j]:
        pol=False
    j-=1
if pol:
    print("Pollindrom")
else:
    print("Not pollindrom")
    
# ex4
import math 
import time 

print("Sample input:")
num = int(input())
ms= int(input())
print("Sample output:")
s= ms/1000
time.sleep(s)
print(f"Square root of {num} after {ms} miliseconds is", math.sqrt(num))

# ex5
tu = tuple(input().split())
b =True

if "False" in tu:
    print("False")
else: 
    print("True")