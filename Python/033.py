def commonDigit(x,y):
    if(x/10 == x%10 or y/10==y%10):
        return 0
    num = str(x)
    den = str(y)
    for a in num:
        for b in den:
            if a==b:
                return a
    return 0

def removeDigit(num, digit):
    temp = str(num)
    temp = temp.replace(str(digit),"")
    temp = int(temp)
    return temp

def gcd(a,b):
    # x is always greater
    if(a > b):
        x,y = a,b
    else:
        x,y = b,a

    while(x%y != 0):
        temp = x
        x = y
        y = temp % x

    return y

# 10/11, 10/12, 10/13, 10/14, 10/15, 10/16, 10/17, 10/18, 10/19, 10/20
# 11/10, 11/11, 11/12, 11/13, 11/14, 11/15, 11/16



fractions = []
for num in range(10,100):
    for den in range(10,100):
        expected = float(num)/den
        if num%10==0 or den%10==0 or num==den or expected >= 1.0 :
            continue
        common = commonDigit(num,den)
        if common:
            num1 = removeDigit(num,common)
            den1 = removeDigit(den,common)
            result = float(num1)/den1
            if expected==result:
                fractions.append([num,den])

num = 1
den = 1
for i in fractions:
    num *= i[0]
    den *= i[1]

print den/gcd(num,den)
