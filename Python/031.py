from itertools import combinations_with_replacement
TARGET = 200
coins = [1,2,5,10,20,50,100,200]

matrix = {}

for y in xrange(0,TARGET+1):
    # for 1 cents is always one way
    matrix[y,0] = 1

for y in xrange(0,TARGET+1):
    print "%3d:%3d" % (y,1),
    for x in range(1,len(coins)):
        matrix[y,x] = 0
        if y>=coins[x]:
            matrix[y,x] += matrix[y,x-1]+matrix[y-coins[x],x]
        else:
            matrix[y,x] = matrix[y,x-1]
        print "%6d" % matrix[y,x],
    print
