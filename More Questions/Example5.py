def pattern(n):
    m=5
    for i in range(0,m):
        for j in range(n+1,i,-1):
            #n+=1
            print(j,end=" ")
        n-=1
        print()


pattern(9)