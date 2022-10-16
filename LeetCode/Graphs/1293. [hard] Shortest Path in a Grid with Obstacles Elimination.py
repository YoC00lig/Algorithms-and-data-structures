"""
You are given an m x n integer matrix grid where each cell is either 0 (empty) or 1 (obstacle). You can move up, down, left, or right from and to an empty cell in one step.

Return the minimum number of steps to walk from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1) given that you can eliminate at most k obstacles. If it is not possible to find such walk return -1.


"""

from collections import deque


def shortestPath(grid, k):
    m, n = len(grid), len(grid[0])
    visited = set()
    q = deque([(0, 0, 0, k)])

    if k >= m + n - 2: return m + n - 2
    while q:
        steps, x, y, obs = q.popleft()
        if x == m - 1 and y == n - 1: return steps

        for r, c in (x, y - 1), (x, y + 1), (x - 1, y), (x + 1, y):

            if 0 <= r < m and 0 <= c < n and obs - grid[r][c] >= 0:
                new = r, c, obs - grid[r][c]
                if new not in visited:
                    visited.add(new)
                    q.append((steps + 1, r, c, obs - grid[r][c]))

    return -1