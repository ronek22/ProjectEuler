'''Longest Collatz sequence'''

def collatz_terms_slower(n):
    count = 0
    while n>1:
        if(n%2==0):
            count+=1
            n = n/2
        else:
            count+=1
            n = 3*n+1
    return count

def collatz_terms(n):
    count = 0
    while n>1:
        if n in visited:
            count += visited[n]
            n=1
        elif(n%2==0):
            count+=1
            n = n/2
        else:
            count+=1
            n = 3*n+1
    return count


number = 3
max_number = 0
max_terms = 0
visited = {1:1,2:2}

while number < 1000000:
    terms = collatz_terms(number)
    visited[number] = terms
    if(terms > max_terms):
        max_terms = terms
        max_number = number
    number+=2 # because odd numbers always have biggest chains

print "Max number is %d and that sequence have %d terms" % (max_number, max_terms)
