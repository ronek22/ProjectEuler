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

# for x in primes:
	


for x in primes:
	perm = list(int(''.join(x)) for x in permutations(str(x)))
	primePerm = set()
	for y in perm:
		if y in primeSet:
			primePerm.add(y)
	print primePerm
	raw_input()
	
	
