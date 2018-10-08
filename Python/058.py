'''Spiral Primes'''
from utility.helper import isPrime
from math import ceil

diag_num = 1
diag_primes = 0
step = 2
x = 3
sides = 3

while True:
    for i in range(4):
        if isPrime(x):
            diag_primes+=1
        diag_num += 1
        x += step
    x -= step
    ratio = int(ceil((float(diag_primes)/diag_num)*100))
    if ratio < 11:
        break
    sides += 2
    step += 2
    x += step

print sides
