"""Print the following inverted staircase pattern based on input size:
Input:
N = 9
Output:
9 8 7 6 5 4 3 2 1
8 7 6 5 4 3 2 1
6 5 4 3 2 1
3 2 1
0
Input:
N = 10
Output:
10 9 8 7 6 5 4 3 2 1
9 8 7 6 5 4 3 2 1
7 6 5 4 3 2 1
4 3 2 1
0 
"""

def pattern(n):
    m=5
    for i in range(0,m):
        for j in range(n+1,i,-1):
            #n+=1
            print(j,end=" ")
        n-=1
        print()


pattern(9)
