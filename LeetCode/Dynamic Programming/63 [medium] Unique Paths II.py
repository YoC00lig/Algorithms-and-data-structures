# You are given an m x n integer array grid. There is a robot initially located
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the
# bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either
# down or right at any point in time.
# An obstacle and space are marked as 1 or 0 respectively in grid. A path
# that the robot takes cannot include any square that is an obstacle.
# Return the number of possible unique paths that the robot can take to reach the bottom-right corner.
# The testcases are generated so that the answer will be less than or equal to 2 * 109


def uniquePathsWithObstacles(obstacleGrid):
    m = len(obstacleGrid)
    n = len(obstacleGrid[0])
    tab = [[0 for _ in range(n)] for _ in range(m)]
    tab[0][0] = 1

    for row in range(m):
        for col in range(n):
            top = row - 1
            left = col - 1
            if top >= 0: tab[row][col] += tab[top][col]
            if left >= 0: tab[row][col] += tab[row][left]
            if obstacleGrid[row][col] == 1: tab[row][col] = 0
    return tab[m - 1][n - 1]