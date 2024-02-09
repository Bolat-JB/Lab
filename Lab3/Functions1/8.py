def spy_game(nums):
    lista = []
    listb = []
    for x in range(0, len(nums)):
        if nums[x] == 0:
            lista.append(x)
        if nums[x] == 7:
            listb.append(x)
    if len(lista) > 1 and len(listb) > 0:
        if listb[0] > lista[0] and listb[0] > lista[1]:
            return True
    return False

print(spy_game([1,2,4,0,0,7,5]))
print(spy_game([1,0,2,4,0,5,7])) 
print(spy_game([1,7,2,0,4,5,0]))