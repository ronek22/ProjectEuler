

def isPandigital(n):
    size = len(n)
    for i in range(1,size+1):
        if str(i) not in n:
            return False
    return True

def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n//2) if sieve[i]]

primes = list(prime_sieve(10**7))
primes = primes[::-1]
maks = 0
for i in primes:
    if isPandigital(str(i)):
        maks = i
        break

print maks
