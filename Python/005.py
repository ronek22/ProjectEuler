'''Smallest multiple'''
def div2to20(number):
	i = 2
	while i<=20:
		if number % i != 0:
			return False
		i+=1
	return True
	
x = 1
while not div2to20(x):
	x+=1

print x
