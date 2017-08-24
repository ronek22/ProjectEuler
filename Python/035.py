# fast generate prime numbers
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n//2) if sieve[i]]



primes = list(prime_sieve(10**6))
primesSet = set(primes)

def rotationsPrime(n):
    number = str(n)
    leng = len(number)

    for i in range(1,leng+1):
        if int(number) in primesSet:
            number=number[1:]+number[:1]
        else:
            return False
    return True




rot = []
for i in primes:
    if rotationsPrime(i):
        rot.append(i)

print len(rot)
