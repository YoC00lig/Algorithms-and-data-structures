"""
Given an n x n integer matrix grid, return the minimum sum of a falling path with non-zero shifts.

A falling path with non-zero shifts is a choice of exactly one element from each row of grid such that
 no two elements chosen in adjacent rows are in the same column.
"""


def minFallingPathSum(grid):
    m, n = len(grid), len(grid[0])

    def FindTwoMins(T):
        min1, min2 = float("inf"), float("inf")
        for num in T:
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        return min1, min2

    for row in range(1, m):
        min1, min2 = FindTwoMins(grid[row - 1])
        for col in range(n):
            if grid[row - 1][col] == min1:
                grid[row][col] += min2
            else:
                grid[row][col] += min1

    return min(grid[-1])