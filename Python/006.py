'''Sum square difference'''
# Brute force solution
"""
sum = 0
sq = 0
for i in range(1,101):
	sum+=i**2
	sq+=i
	
sq = sq**2

print sq - sum
"""
# More more efficient solution involve algebra
n = 100
suma = n*(n+1)/2
sum_sq = (2 * n + 1)*(n + 1)*n/6
print suma**2 - sum_sq
