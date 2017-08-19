def ch2int(c):
    #only works for big letters
    return ord(c)-64

f = open('p022_names.txt', 'r')
txt = f.read()
content = []
for name in txt.split(','):
    content.append(name[1:len(name)-1]) # delete quotation marks
f.close()

i=1
total = 0
content.sort()
for name in content:
    suma = 0
    for c in name:
        suma+=ch2int(c)
    suma*=i
    total+=suma
    i+=1

print total
    
