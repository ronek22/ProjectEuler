'''Pandigital products'''
#21 s
def isPandigital(n):
    for i in range(1,10):
        if str(i) not in n:
            return False
    return True
suma = set()
for x in range(1,1000):
    for y in range(1,10000):
        product = x*y
        string = str(x)+str(y)+str(product)
        lenght = len(string)
        if lenght>9:
            break
        if lenght == 9:
            if isPandigital(string):
                suma.add(product)

print sum(suma)
