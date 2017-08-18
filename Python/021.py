def sumDivisors(n):
    listDiv = []
    for i in range(1,n):
        if(n%i==0):
            listDiv.append(i)
    return sum(listDiv)

amicable = []
for i in range(9999,0,-1):
    a = sumDivisors(i) # i - 220, a = 284
    if(a==i):
        continue
    b = sumDivisors(a) # b = 220

    if(b==i):
        if not a in amicable:
            amicable.append(a)
        if not b in amicable:
            amicable.append(b)

print sum(amicable)
