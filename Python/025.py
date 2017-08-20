import time
def FibonacciRec(n):
    if n==1 or n==2:
        return 1
    return FibonacciRec(n-1)+FibonacciRec(n-2)

def FibonacciIte(n):
    fibs=[0,1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs[n]

def fibDig(digits):
    fibs=[0,1,1]
    i=2
    length = 1
    while length < digits:
        f = fibs[-1]+fibs[-2]
        fibs.append(f)
        length = len(str(f))
        i+=1
    return fibs[i],i


# print FibonacciIte(12)
fib, term = fibDig(1000)
print "Index of first term to contain 1000 digits is: %d\nF(%d) = %d" % (term,term,fib)
