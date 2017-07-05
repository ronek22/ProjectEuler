def isPalindrome(number):
	x = str(number)
	n = len(x)
	i = 0
	while i < n:
		if x[i] != x[n-i-1]:
			return False
		i += 1
	
	return True
	
wynik = []

for x in range(100,1000):
	for y in range(100,1000):
		test = x * y
		if isPalindrome(test):
			wynik.append(test)
			
print max(wynik)
