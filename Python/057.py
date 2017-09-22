'''Square root convergents'''
LIMIT = 1000
def comp_num_len(first, second):
    '''Compare two numbers'''
    n = len(str(first))
    d = len(str(second))
    if n > d:
        return 1
    elif n < d:
        return -1
    else:
        return 0


# To calculate term, we must have two previous terms

numerators = [3, 7]
denominators = [2, 5]

# formula for numerators: n(k) = 2*n(k-1)+n(k-2)
# formula for denominators: d(k) = 3*d(k-1)-n(k-2)

for i in range(2, LIMIT+1):
    num = 2*numerators[i-1]+numerators[i-2]
    den = 3*denominators[i-1]-numerators[i-2]

    numerators.append(num)
    denominators.append(den)


FRACT = 0
for i in xrange(LIMIT+1):
    if comp_num_len(numerators[i], denominators[i]) == 1:
        FRACT += 1

print FRACT
