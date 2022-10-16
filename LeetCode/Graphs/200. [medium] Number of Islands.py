"""
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
You may assume all four edges of the grid are all surrounded by water.
"""


def numIslands(grid):
    if not grid: return 0

    def DFS(grid, row, col):
        if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and grid[row][col] == '1':
            grid[row][col] = '0'
            DFS(grid, row + 1, col)
            DFS(grid, row - 1, col)
            DFS(grid, row, col + 1)
            DFS(grid, row, col - 1)

    isLand = 0

    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '1':
                DFS(grid, row, col)
                isLand += 1
    return isLand