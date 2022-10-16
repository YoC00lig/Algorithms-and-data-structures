# Given a triangle array, return the minimum path sum from top to bottom.
# For each step, you may move to an adjacent number of the row below.
# More formally, if you are on index i on the current row, you may move
# to either index i or index i + 1 on the next row.

# Input: triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
# Output: 11
# Explanation: The triangle looks like:
#    2
#   3 4
#  6 5 7
# 4 1 8 3
# The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11 (underlined above).

def minimumTotal(triangle):
    n = len(triangle)
    tab = [[float('inf') for _ in range(n)] for _ in range(n)]
    tab[0][0] = triangle[0][0]
    for row in range(1, n):
        for col in range(row + 1):
            if col - 1 >= 0:
                tab[row][col] = min(tab[row][col], tab[row - 1][col - 1] + triangle[row][col], tab[row - 1][col] + triangle[row][col])
            else:
                tab[row][col] = min(tab[row][col], tab[row - 1][col] + triangle[row][col])
    return min(tab[n - 1])