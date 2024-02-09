from itertools import permutations

def permutation(a):
    s = permutations(a)
    for i in s:
        print(i)
    
st = str(input())
print(permutation(st))