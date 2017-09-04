def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n//2) if sieve[i]]
    
primes = list(prime_sieve(10**6))
primeSet = set(primes)

fP = []

suma = 0
for x in primes:
	suma+=x
	if suma>1000000: break
	fP.append(suma)

result = 0	
n = len(fP)

for i in range(n-1,-1,-1):
	for j in range(n):
		x = fP[i]-fP[j]
		if x < result: break
		if x in primes:
			result = x

print result
