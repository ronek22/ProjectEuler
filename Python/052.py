def isPermutation(x,y):
    x,y = str(x),str(y)
    return (len(x)==len(y)) and (sorted(x)==sorted(y))

# def isP(x,y):
#     x,y = str(x),str(y)
#     if len(x)!=len(y):
#         return False

#
# print isPermutation(2155,1255)
x = 1
cond = True
while cond:
    for i in range(2,7):
        if not isPermutation(x,i*x):
            break
        if i==6:
            print x
            cond = False
    x+=1
