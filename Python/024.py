'''Lexicographic permutations'''
import itertools
import time

def slowPermut():
    a = list(itertools.permutations(range(10)))[999999]
    print ''.join(str(x) for x in a)


def quickPermut():
    # when the first left digit is 0, we have 362880 possibilites
    # so when the first left digits is 2, we can reach milionth permutaions,
    #it will be 274240nth permutation
    a = list(itertools.permutations([0,1,3,4,5,6,7,8,9]))[274239]
    milionth = '2'+''.join(str(x) for x in a)
    print milionth

def timeCount(func):
    start_time = time.time()
    func()
    end_time = time.time()
    total_time = end_time-start_time
    print "TIME: %f\n" % total_time

print "SLOW"
timeCount(slowPermut)
print "FAST"
timeCount(quickPermut)
