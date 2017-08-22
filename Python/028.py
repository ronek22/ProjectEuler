def diagSum(tab,x,y,n):
    if(x==y):
        return tab[x][y]
    elif(x+y==n-1):
        return tab[x][y]
    else:
        return 0

def spiral(n):
    if(n%2==0):
        print "MUST BE ODD NUMBER"
        return
    w,h = n,n;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    start = n/2
    x=y=start
    number = 2
    Matrix[x][y]=1

    dire = 0
    # 0 - right
    # 1 - down
    # 2 - left
    # 3 - up

    suma = 1
    while not((x==0 and y==n-1)):
        if(dire==0):
            y+=1
            Matrix[x][y]=number
            suma+=diagSum(Matrix,x,y,n)
            if(Matrix[x+1][y]==0):
                change=True
            else:
                change=False
        elif(dire==1):
            x+=1
            Matrix[x][y]=number
            suma+=diagSum(Matrix,x,y,n)
            if(Matrix[x][y-1]==0):
                change=True
            else:
                change=False
        elif(dire==2):
            y-=1
            Matrix[x][y]=number
            suma+=diagSum(Matrix,x,y,n)
            if(Matrix[x-1][y]==0):
                change=True
            else:
                change=False
        elif(dire==3):
            x-=1
            Matrix[x][y]=number
            suma+=diagSum(Matrix,x,y,n)
            if(Matrix[x][y+1]==0):
                change=True
            else:
                change=False
        if change:
            dire = (dire+1)%4
        number+=1
    printMatrix(Matrix)
    print suma

def printMatrix(tab):
    rows = len(tab)
    columns = len(tab[0])
    if(rows<12):
        for i in range(0,rows):
            for j in range(0,columns):
                print "%6d" % tab[i][j],
            print ""
    else:
        save = str(raw_input("SAVE SPIRAL TO FILE?[y][n]"))
        if save.lower() == 'y':
            f = open('spiral028.txt','w')
            for i in range(0,rows):
                for j in range(0,columns):
                     f.write("%13d" % tab[i][j],)
                f.write('\n')
            print "Matrix print into spiral028.txt file!"

spiral(1001)
