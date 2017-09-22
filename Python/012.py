'''Highly divisible triangular number'''
from math import sqrt
# too slow for n > 200
def simpleCountDivisors(n):
    # listDiv = []
    numOfDiv = 0
    for i in range(1,n+1):
        if(n%i==0):
            # listDiv.append(i)
            numOfDiv+=1
    # numOfDiv = len(listDiv)
    # print str(n)+": ",
    # for d in listDiv:
        # print d,
    return numOfDiv

def countDivisors(n):
    nod = 0 # number of divisors
    nSqrt = int(sqrt(n))

    for i in range(1,nSqrt+1):
        if(n%i==0):
            nod+=2

    if (nSqrt*nSqrt == n):
        nod-=1

    return nod


def test(x):
    n=0
    number = 0
    i=1
    while countDivisors(number) <= x:
        number+=i
        i+=1
    return number


print test(500)
