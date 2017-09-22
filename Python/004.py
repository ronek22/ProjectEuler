'''Largest palindrome product'''
import time

def isPalindrome(number):
	x = str(number)
	n = len(x)
	i = 0
	while i < n:
		if x[i] != x[n-i-1]:
			return False
		i += 1

	return True

def PalindromTest1():
	wynik = []

	for x in range(100,1000):
		for y in range(100,1000):
			test = x * y
			if isPalindrome(test):
				wynik.append(test)

	print max(wynik)

def PalindromTest2():
	wynik = 0
	for x in range(1000,100,-1):
		if x*x < wynik:
			break
		for y in range(1000,100,-1):
			test = x*y
			if isPalindrome(test):
				if(test > wynik):
					wynik = test
	print wynik

print "#1 Algorytm"
print '-'*15
start_time=time.time()
PalindromTest1()
total_time = time.time() - start_time
print "CZAS: ", total_time

print '\n'

print "#2 Algorytm"
print '-'*15
start_time=time.time()
PalindromTest2()
total_time2 = time.time() - start_time
print "CZAS: ", total_time2

quicker = (total_time-total_time2)/total_time*100
print "\nAlgorytm #2 szybszy o %d%%" % quicker
