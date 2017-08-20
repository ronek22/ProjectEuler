from math import sqrt; from itertools import count,islice

def isPrime(n):
	return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

#below n
def generatePrime(n):
    primes = []
    for i in range(n,7,-1):
        if isPrime(i):
            primes.append(i)
    return primes

p = generatePrime(1000)
# print p

for i in p:
    x = 0
    n=0
    while x!=1:
        n+=1
        #all primes except 2,5
        x = (10**n)%i
    print "1/%d cycle = %d" % (i,n)
