from itertools import permutations

pan = permutations("1234567890")
prime = [2,3,5,7,11,13,17]
div = []

for i in pan:
    cond = True
    if i[0]=="0":
        break

    for j in range(1,8):
        if int(i[j]+i[j+1]+i[j+2])%prime[j-1] != 0:
            cond = False
            break

    if cond:
        number = ''.join(i)
        div.append(int(number))

print sum(div)
