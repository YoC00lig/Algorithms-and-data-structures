# Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
# The distance between two adjacent cells is 1.


# Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
# Output: [[0,0,0],[0,1,0],[1,2,1]]

def updateMatrix(mat):
    n = len(mat)
    m = len(mat[0])
    matrix = [[float('inf') for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if mat[i][j] == 0:
                matrix[i][j] = 0

            else:
                if i > 0: matrix[i][j] = min(matrix[i][j], matrix[i - 1][j] + 1)
                if j > 0: matrix[i][j] = min(matrix[i][j], matrix[i][j - 1] + 1)

    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            if i < n - 1: matrix[i][j] = min(matrix[i][j], matrix[i + 1][j] + 1)
            if j < m - 1: matrix[i][j] = min(matrix[i][j], matrix[i][j + 1] + 1)

    return matrix