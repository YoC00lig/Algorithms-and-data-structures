"""
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex (i.e., clockwise order).

You will triangulate the polygon into n - 2 triangles. For each triangle, the value of that triangle is the product of the values of its vertices, and the total score of the triangulation is the sum of these values over all n - 2 triangles in the triangulation.

Return the smallest possible total score that you can achieve with some triangulation of the polygon.

"""


def minScoreTriangulation(values):
    def multiply(M1, M2):
        return M1[0] * M1[1] * M2[1]

    def MCM(T):
        n = len(T)
        dp = [[float("inf")] * n for _ in range(n)]
        m = [[(None, None)] * n for _ in range(n)]

        for i in range(n):
            dp[i][i] = 0
            m[i][i] = (T[i][0], T[i][1])

        for i in range(n - 1):
            dp[i][i + 1] = multiply(T[i], T[i + 1])
            m[i][i + 1] = (T[i][0], T[i + 1][1])

        for i in range(n - 2, -1, -1):
            for j in range(i + 1, n):
                for k in range(i, j):
                    if dp[i][j] > dp[i][k] + dp[k + 1][j] + multiply(m[i][k], m[k + 1][j]):
                        dp[i][j] = dp[i][k] + dp[k + 1][j] + multiply(m[i][k], m[k + 1][j])
                        m[i][j] = (m[i][k][0], m[k + 1][j][1])
        return dp[0][-1]

    t = []

    for i in range(len(values) - 1):
        t.append((values[i], values[i + 1]))

    return MCM(t)