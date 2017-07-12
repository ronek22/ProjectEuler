from math import sqrt; from itertools import count,islice

def isPrime(n):
	return n>1 and all(n%i for i in islice(count(2), int(sqrt(n)-1)))
	
wynik = 0
i = 2
while i < 2000000:
	if isPrime(i):
		wynik+=i
	i+=1
	
print wynik
