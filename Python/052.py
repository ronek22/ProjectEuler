'''Permuted multiples'''
def is_permutation(x, y):
    ''' Check if both numbers are permutations of each other'''
    x, y = str(x), str(y)
    return (len(x) == len(y)) and (sorted(x) == sorted(y))


x = 1
COND = True
while COND:
    for i in range(2,7):
        if not is_permutation(x,i*x):
            break
        if i==6:
            print x
            COND = False
    x+=1
