'''Lychrel numbers'''
def isPalindrome(s):
    return s == s[::-1]


def reverse(x):
    '''Reverse number'''
    rev = str(x)[::-1]
    return int(rev)


lynchel = []
for x in range(10001):
    count = 0
    temp = x+reverse(x)
    while count < 50:
        if isPalindrome(str(temp)):
            break
        else:
            count+=1
            temp=temp+reverse(temp)
    if count == 50:
        lynchel.append(x)

print len(lynchel)
            
        
