comb = []
for a in range(2,101):
    for b in range(2,101):
        comb.append(a**b)

print len(sorted(set(comb)))
