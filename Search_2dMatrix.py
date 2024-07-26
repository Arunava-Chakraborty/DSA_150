matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3


def searchMatrix(matrix, target):
        n = len(matrix)
        m = len(matrix[0])
        for i in range(n):
            for j in range(m):
                if(matrix[i][j] == target):
                    return True
                
print(searchMatrix(matrix , target))

        