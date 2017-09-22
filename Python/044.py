'''Pentagon numbers'''
#044
from datetime import datetime

def pentagon(n):
	return n*(3*n-1)/2

start_time = datetime.now()
pent = []
for i in range(1,3000):
	pent.append(pentagon(i))

pentSet = set(pent)
	
length = len(pent)
for j in range(0,length):
	for k in range(j+1,length):
		suma = pent[j]+pent[k]
		diff = pent[k]-pent[j]
		if(suma in pentSet and diff in pentSet):
			print pent[j], pent[k], " = ", abs(pent[j]-pent[k])
			
# do your work here
end_time = datetime.now()
print('Duration: {}'.format(end_time - start_time))
