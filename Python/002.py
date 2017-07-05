# return value of nth fibonacci number
def fibonacci(n):
	if n==1:
		return 1
	elif n==2:
		return 2
	else:
		return fibonacci(n-1)+fibonacci(n-2)
		

sum = 0; i = 1
x = fibonacci(i)

while x < 4000000:
	if x%2 == 0:
		sum+=x
	
	i+=1
	x = fibonacci(i)
	
print sum
							
