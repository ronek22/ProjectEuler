sum = 0
sq = 0
for i in range(1,101):
	sum+=i**2
	sq+=i
	
sq = sq**2

print sq - sum
