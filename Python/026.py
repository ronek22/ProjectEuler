from math import sqrt
import os
import time
from itertools import count,islice

MAX = 1000

def isPrime(n):
	return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))

#below n
def generatePrime(n):
    primes = []
    for i in range(n,6,-1):
        if isPrime(i):
            primes.append(i)
    return primes

def solutionPrimes():
    p = generatePrime(MAX)
    maks_i = 0
    maks = 0
    for i in p:
        x = 0
        n=0
        while x!=1:
            n+=1
            x=pow(10,n,i)
        if(n>maks):
            maks=n
            maks_i = i
        if(n==i-1):
            break
        # print "1/%d cycle = %d" % (i,n)
    print maks_i

def solutionByHand():
    max_cycle=0
    for i in range(MAX,1,-1):
        remainders = set()
        remainders.add(1)
        rem = 10%i
        while rem not in remainders:
            remainders.add(rem)
            if rem==0:
                remainders.clear()
                break
            rem = (rem*10)%i
        cycle = len(remainders)
        if cycle>max_cycle:
            max_cycle = cycle
            number = i
        #cycle length < i
        if cycle==i-1:
            break
    print number



def timeCount(func):
    start_time = time.time()
    func()
    end_time = time.time()
    total_time = end_time-start_time
    print "TIME: %f\n" % total_time

print "BY HAND\nLOOP %d to 1" % MAX
timeCount(solutionByHand)
print "USING FERMAT LOOP ONLY PRIMES"
timeCount(solutionPrimes)
