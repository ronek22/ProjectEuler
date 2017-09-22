'''Truncatable primes'''
# fast generate prime numbers
def prime_sieve(n):
    sieve = [True] * (n//2)
    for i in xrange(3, int(n**0.5)+1,2):
        if sieve[i//2]:
            sieve[i*i//2::i] = [False]*((n-i*i-1)//(2*i)+1)
    return [2] + [2*i+1 for i in xrange(1, n//2) if sieve[i]]



primes = list(prime_sieve(1000000))
primesSet = set(primes)

def rotationsPrime(n):
    number = str(n)
    leng = len(number)

    for i in range(1,leng):
        numberRight=number[i:]
        numberLeft=number[:-i]
        # print numberRight,numberLeft
        if not (int(numberRight) in primesSet and int(numberLeft) in primesSet):
            return False
    return True




rot = []
for i in primes[8:]:
    if rotationsPrime(i):
        rot.append(i)

print sum(rot)
