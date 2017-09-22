'''Integer right triangles'''
maxSol = 0
max_p = 0
p = 110
for p in range(110,1000):
    sol = []
    for a in range(3,(p/3)):
        if ((2*p*a)-p*p)%(2*a-2*p) == 0:
            b = ((2*p*a)-p*p)/(2*a-2*p)
            if a>b:
                continue
        else:
            continue
        c = p-a-b
        sol.append([a,b,c])
    amount = len(sol)
    if amount>maxSol:
        maxSol = amount
        max_p = p

print max_p,maxSol
