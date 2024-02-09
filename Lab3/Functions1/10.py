def unique(l):
    unique_list = []
    for i in l:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

n = int(input())
list1 = []
for i in range(n):
    li = int(input())
    list1.append(li)
    
print(unique(list1))