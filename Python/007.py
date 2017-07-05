from math import sqrt; from itertools import count,islice

def isPrime(n):
	return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	
wynik = 0
i = 2
while wynik != 10001:
	if isPrime(i):
		wynik+=1
	i+=1
	
print i-1
	
