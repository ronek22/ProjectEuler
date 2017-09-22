'''Digit fifth powers'''
find = []
for i in range(2,1000000):
    num = str(i)
    powerSum = 0
    for j in num:
        powerSum+=int(j)**5
    if powerSum==i:
        find.append(i)

print sum(find)
