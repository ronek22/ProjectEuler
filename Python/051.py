from itertools import permutations


def sieve_gen(lower, limit):
    ''' return prime number list in range(lower,limit)'''
    sievebound = (limit) / 2  # last index of sieve
    sieve = [False] * (sievebound + 1)
    crosslimit = (int(limit**0.5) - 1) / 2

    for i in xrange(1, crosslimit):
        if not sieve[i]:  # 2i+1 is prime, mark multiples
            for j in xrange(2 * i * (i + 1), sievebound, 2 * i + 1):
                sieve[j] = True

    primes = [2] if lower <= 2 else []

    for i in xrange(1, sievebound):
        if 2 * i + 1 < lower:
            continue
        if not sieve[i]:
            primes.append(2 * i + 1)
    return primes


def mask():
    ''' Generate permutations for 6 digits number with 3 masked digits''' 
    f = open('test.txt', 'w')
    b = set(permutations("ABCxxx"))
    for i in b:
        z = 0
        for j in i:
            if j == 'A':
                iA = z
            elif j == 'B':
                iB = z
            elif j == "C":
                iC = z
            z += 1
        if iA < iB < iC:
            t = ''.join(i)
            f.write('"' + t + '"' + ',')


masks = ["ABxCxx", "ABCxxx", "xxxABC", "ABxxxC", "xAxBCx",
         "xAxBxC", "AxxxBC", "xABxCx", "AxBxCx", "xABxxC",
         "xxAxBC", "xxABxC", "AxxBCx", "xAxxBC", "xxABCx",
         "xABCxx", "AxBCxx", "AxBxxC", "ABxxCx", "AxxBxC"]

prime = sieve_gen(10**5, 10**6)
primeSet = set(prime)

for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for m in masks:
                family, count, t = [], 0, m
                t = t.replace('A', str(a)).replace('B',str(b)).replace('C',str(c))
                if (t[0] == '0'): continue # firts digit cannot be 0

                for x in range(0, 10):
                    temp = t.replace('x', str(x))
                    if temp[0] != '0':
                        cand = int(temp)
                        if cand in primeSet:
                            family.append(cand)
                            count += 1
                if count == 8:
                    print min(family)
                    break
