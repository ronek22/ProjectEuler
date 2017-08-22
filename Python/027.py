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
for a in range(1,1000):
    for b in range(1,1000):
        n=0
        counted = 0
        while True:
            p = n*n+a*n+b
            if p in primes:
                counted+=1
                n+=1
            else:
                # print "For n^2+%d+%d, sequence has: %d primes" % (a,b,count)
                if(counted>max_count):
                    max_count = counted
                    formula = "n^2 + %dn + %d" % (a,b)
                    max_a = a
                    max_b = b
                break

        n=0
        counted = 0
        while True:
            p = n*n-a*n+b
            if p in primes:
                counted+=1
                n+=1
            else:
                # print "For n^2-%d+%d, sequence has: %d primes" % (a,b,count)
                if(counted>max_count):
                    max_count = counted
                    formula = "n^2 - %dn + %d" % (a,b)
                    max_a = -a
                    max_b = b
                break

        n=0
        counted = 0
        while True:
            p = n*n+a*n-b
            if p in primes:
                counted+=1
                n+=1
            else:
                # print "For n^2+%d-%d, sequence has: %d primes" % (a,b,count)
                if(counted>max_count):
                    max_count = counted
                    max_a = a
                    max_b = -b
                    formula = "n^2 + %dn - %d" % (a,b)
                break

        n=0
        counted = 0
        while True:
            p = n*n-a*n-b
            if p in primes:
                counted+=1
                n+=1
            else:
                # print "For n^2-%d-%d  sequence has: %d primes" % (a,b,count)
                if(counted>max_count):
                    max_a = -a
                    max_b = -b
                    max_count = counted
                    formula = "n^2 - %dn - %d" % (a,b)
                break

print "FORMULA: %s has %d primes" % (formula,max_count)
print "PRODUCT = %d" % (max_a*max_b)
