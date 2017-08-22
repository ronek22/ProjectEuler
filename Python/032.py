suma = set()
for x in range(1,1000):
    for y in range(1,10000):
        product = x*y
        string = str(x)+str(y)+str(product)
        lst = [int(i) for i in string]
        if 0 in lst:
            continue
        l = len(lst)
        if l>9:
            break
        if l==9:
            if l == len(set(lst)):
                suma.add(product)

print sum(suma)
