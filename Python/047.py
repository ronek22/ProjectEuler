import primefac

count = 0
i = 1

while count < 4:
	factors = set(primefac.primefac(i))
	if count == 1 or count == 2 or count == 3:
		if len(factors) != 4:
			count = 0
			continue
		else:
			count+=1
			if count==4:
				print i-3,i-2,i-1,i
	else:
		if len(factors) == 4:
			count+=1
			i+=1
			continue
	i+=1
