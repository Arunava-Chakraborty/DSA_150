matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
def setZeroes(matrix):
        
        n = len(matrix)       # Number of rows
        m = len(matrix[0])    # Number of columns
        row = [0]* n 
        col = [0] * m

        for i in range (n):
            for j in range(m):
                if(matrix[i][j] == 0):
                    row[i] = 1
                    col[j] = 1

        for i in range  (n):
            for j in range (m):
                if(row[i] or col[j] == 1):
                    matrix[i][j] =0
        
        return matrix

print(setZeroes(matrix))
