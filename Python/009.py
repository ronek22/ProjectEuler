'''Special Pythagorean triplet'''
for a in range(0,333):
	for b in range(a+1,500):
		c = 1000 - a - b
		if(a*a + b*b == c*c and (a+b+c)==1000):
			print "a = %d, b = %d, c = %d" % (a,b,c)
			print "abc = %d" % (a*b*c)
			break

# while suma != 1000:
	
# 	if a%2 == 0:
# 		b = (a/2)**2-1
# 		c = b+2
# 	else:
# 		b = (a**2-1)/2
# 		c = b+1
	
# 	suma = a+b+c
# 	print a, " ", b, " ", c
# 	print "SUMA = %d" % suma
# 	if(suma == 1000 and a**2+b**2==c**2):
# 		print "suma = %d\na = %d\nb= %d\n c=%d\n" % (suma,a,b,c)
		
# 	a+=1
	
