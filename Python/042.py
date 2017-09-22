'''Coded triangle numbers'''
def ch2int(c):
    #only works for big letters
    return ord(c)-64

def genTriWord(n):
    tri = set()
    for i in range(1,n+1):
        t = int((0.5)*i*(i+1))
        tri.add(t)
    return tri

triWord = genTriWord(20)

f = open('p042_words.txt', 'r')
txt = f.read()
content = []
for name in txt.split(','):
    content.append(name[1:len(name)-1]) # delete quotation marks
f.close()

i=1
total = 0
max_suma = 0
for name in content:
    suma = 0
    for c in name:
        suma+=ch2int(c)
    if suma in triWord:
        total+=1

print total
