LIMIT = 10000
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n//2) if sieve[i]]

primes = set(prime_sieve(LIMIT))
primes = sorted(primes)
def test(n):
	for i in primes:
		if i>n:
			return False
		j = 1	
		x = i+(2*(j**2))
		while x<=n:
			if x==n:
				# print "%-3d=%3d + 2 *%2d^2" % (n,i,j)
				return True
			j+=1
			x = i+(2*(j**2))

odd = []

for i in range(3,LIMIT,2):
	if not i in primes:
		odd.append(i)
		
		
for i in odd:
	if test(i):
		pass
	else:
		print "BLAD", i

