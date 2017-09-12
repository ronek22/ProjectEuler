from math import factorial
def comb(n, r):
    '''Return combination evaluation'''
    return (factorial(n))/(factorial(r)*factorial(n-r))

greater = 0
for n in range(1, 101):
    for r in range(1, n+1):
        if comb(n, r) > 10**6:
            greater += 1

print greater
