"""
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""
facs = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

suma = 0
for i in range(3,2540161):
    temp = str(i)
    curious = 0
    for y in temp:
        curious+=facs[int(y)]
    # print i,curious
    if curious==i:
        suma+=i

print suma
