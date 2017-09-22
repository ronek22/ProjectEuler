'''Non-abundant sums'''
import math
#perfect number:     sum of its proper divisors = number
#deficient number:   sum of its proper divisors < number
#abundant number:    sum of its proper divisors > number
def sumDiv(n):
    if n==1: return 0
    r = int(math.sqrt(n))
    # assume that n is a perfect square
    if r*r==n:
        suma=1+r
        r-=1
    else:
        suma=1

    if(n%2==0):
        f = 2
        step = 1
    else:
        f = 3
        step = 2

    while f<=r:
        if n%f==0:
            suma+=f+(n/f)
        f+=step
    return suma

def abundantNumber(n):
    if sumDiv(n)>n:
        return True
    else:
        return False
def isAbundantSum(n):
    for i in abundants:
        if i>n:
            return False
        if (n-i) in abundants:
            return True
    return False

# sets for this problem was significant faster
abundants = set()
suma = 0
#its enough to iterate only 20161 times
for i in range(1,20162):
    if abundantNumber(i):
        abundants.add(i)
    if isAbundantSum(i):
        continue
    suma+=i

print suma
