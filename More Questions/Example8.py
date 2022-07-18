"""Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
You must do it in place (do not return anything).
Input: matrix = [[1,1,1],
                 [1,0,1],
                 [1,1,1]]
Output: [[1,0,1],
         [0,0,0],
         [1,0,1]]
"""

def add_zeros(matrix:list):
    r=len(matrix)
    c=len(matrix[0])
    rows,cols=set(),set()
    for i in range(r):
        for j in range(c):
            #print(matrix[i][j])
            if matrix[i][j]==0:
                rows.add(i)
                cols.add(j)
    for i in range(r):
        for j in range(c):
            if i in rows or j in cols:
                matrix[i][j]=0
    print(rows)
    print(cols)


matrix = [[1,1,1], [1,0,1], [1,1,1]]
add_zeros(matrix)
print(matrix)