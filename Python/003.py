import math # learn more: https://python.org/pypi/Math

"""
def FermatFactor(n):
	a = math.ceil(math.sqrt(n))
	b2 = a*a - n
	#print "A = ", a
	#print "B2 = ", b2
	#do it, until b2 is not a perferct square
	while math.sqrt(b2) - int(math.sqrt(b2)) != 0:

		a += 1
		b2 = a * a - n
		#print "A = ", a
		#print "B2 = ", b2
		#raw_input("WAIT")

	return a + math.sqrt(b2)
"""

def prime(n,a):
	i = a
	while (n%i != 0 and i*i<n):
		i+=1
	if(i*i<n):
		return prime(n/i, i)
	else:
		print("The highest prime factor is: "),n
		

prime(600851475143,2)
