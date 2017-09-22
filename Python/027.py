'''Quadratic primes'''
from math import sqrt; from itertools import count,islice

def isPrime(n):
	return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

primes = set()
for i in range(1,10000):
    if isPrime(i):
        primes.add(i)

max_count = 0
formula = ""
max_a = 0
max_b = 0
for a in range(-999,1000):
    for b in range(-1000,1001):
        n=0
        while (n*n+a*n+b) in primes:
            n+=1
        if(n>max_count):
            max_count = n
            formula = "n^2 + %dn + %d" % (a,b)
            max_a, max_b = a,b
print "FORMULA: %s has %d primes" % (formula,max_count)
print "PRODUCT = %d" % (max_a*max_b)
