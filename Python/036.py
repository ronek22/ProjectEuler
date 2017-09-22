'''Double-base palindromes'''
def isPalindrome(x):
	n = len(x)
	i = 0
	while i < n:
		if x[i] != x[n-i-1]:
			return False
		i += 1
	return True

palindroms = []
for i in range(1,10**6):
    if isPalindrome(str(i)):
        if isPalindrome(bin(i)[2:]):
            palindroms.append(i)
print sum(palindroms)
