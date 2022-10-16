"""
You are given a 0-indexed 2D integer array grid of size m x n. Each cell has one of two values:

0 represents an empty cell,
1 represents an obstacle that may be removed.
You can move up, down, left, or right from and to an empty cell.

Return the minimum number of obstacles to remove so you can move from the upper left corner (0, 0) to the lower right corner (m - 1, n - 1).


"""

from collections import deque
def minimumObstacles(grid):
    R, C = len(grid), len(grid[0])

    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    distances = [[-1] * C for _ in range(R)]

    q = deque([(0, 0, 0)])

    while q:
        dist, r, c = q.popleft()

        for dr, dc in d:
            rr, cc = r + dr, c + dc
            if 0 <= rr < R and 0 <= cc < C and distances[rr][cc] == -1:
                if grid[rr][cc] == 1:
                    distances[rr][cc] = dist + 1
                    q.append((dist + 1, rr, cc))

                else:
                    distances[rr][cc] = dist
                    q.appendleft((dist, rr, cc))

    return distances[R - 1][C - 1]