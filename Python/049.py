'''Prime permutations'''
from itertools import permutations

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n//2) if sieve[i]]
    
primes = list(prime_sieve(10000))
primes = primes[168:]
primeSet = set(primes)

for x in primes:
	found = False
	arithm = []
	perm = list(int(''.join(x)) for x in permutations(str(x)))
	primePerm = set()
	for y in perm:
		if y in primeSet:
			primePerm.add(y)
			primes.remove(y)
			primeSet.remove(y)
	primePerm = sorted(list(primePerm))
	
	for x in range(0,len(primePerm)-2):
		third = primePerm[x+1]+(primePerm[x+1]-primePerm[x])
		if third == primePerm[x+2]:
			found = True
			arithm.append([primePerm[x],primePerm[x+1],primePerm[x+2]])
	
	if found:
		print str(arithm[0][0])+str(arithm[0][1])+str(arithm[0][2])	
