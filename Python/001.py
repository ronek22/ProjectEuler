'''Multiples of 3 and 5'''
print "The sum of all the multiples of 3 or 5 below 1000."
print '-' * 25

sum = 0
for i in range(1,1000):
	if (i%3 == 0) or (i%5 == 0):
		sum+=i

print "Sum = ",sum
