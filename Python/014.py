def collatz_terms_rec(n,count=0):
    if(n==1):
        count+=1
        return count
    elif(n%2==0):
        count+=1
        return collatz_terms(n/2,count)
    else:
        count+=1
        return collatz_terms(3*n+1,count)

def collatz_terms2(n):
    count = 0
    while n>1:
        if n in visited_collatz.keys():
            count += visited_collatz[n]
            break;
        elif(n%2==0):
            count+=1
            n = n/2
        else:
            count+=1
            n = 3*n+1
    return count

def collatz_terms(n):
    count = 0
    while n>1:
        if(n%2==0):
            count+=1
            n = n/2
        else:
            count+=1
            n = 3*n+1
    return count



number = 1
max_number = 0
max_terms = 0
# visited_collatz = {}

while number < 1000000:
    terms = collatz_terms(number)
    # visited_collatz[number] = terms
    # print "%d\t%d" % (number,terms)
    if(terms > max_terms):
        max_terms = terms
        max_number = number
    number+=1

print "Max number is %d and that sequence have %d terms" % (max_number, max_terms)
