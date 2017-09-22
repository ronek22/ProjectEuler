'''Pandigital multiples'''
def isPandigital(n):
    for i in range(1,10):
        if str(i) not in n:
            return False
    return True

pan = []
for i in range(2,10000):
    j=1
    suma=str(i*j)
    while len(suma)<9:
        j+=1
        suma+=str(i*j)
    if(len(suma)>9):
        continue
    if isPandigital(suma):
        pan.append(suma)

print max(pan)
