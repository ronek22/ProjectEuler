'''
A googol (10^100) is a massive number: one followed by one-hundred zeros.
100^100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, a^b, where a, b < 100, what is the maximum digital sum?
'''

def sum_digit(number):
    '''Return sum of digits in number'''
    num = str(number)
    sum_d = 0
    for digit in num:
        sum_d += int(digit)

    return sum_d

max_d = 0
for a in range(1, 100):
    for b in range(1, 100):
        candidate = sum_digit(pow(a, b))
        if candidate > max_d:
            max_d = candidate

print max_d
