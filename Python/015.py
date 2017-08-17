def countWays(n):
    w,h = n+1,n+1;
    Matrix = [[0 for x in range(w)] for y in range(h)]
    # 1 on the edges without end point
    for i in range(0,n):
        Matrix[i][n] = 1;
        Matrix[n][i] = 1;

    for i in range(n-1,-1,-1):
        for j in range(n-1,-1,-1):
            Matrix[i][j] = Matrix[i+1][j]+Matrix[i][j+1]
    print "FINAL:"
    printMatrix(Matrix)
    return Matrix[0][0]

def printMatrix(tab):
    rows = len(tab)
    columns = len(tab[0])
    for i in range(0,rows):
        for j in range(0,columns):
            print "%6d" % tab[i][j],
        print ""

grid = 3
ways = countWays(grid)
print "For %dx%d there are %d possible paths" % (grid,grid,ways)
