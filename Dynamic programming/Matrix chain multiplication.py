def multiply(M1, M2):
    return M1[0] * M1[1] * M2[1]

def MCM(T):
    n = len(T)
    dp = [[float("inf")] * n for _ in range(n)]
    m_size = [[(None, None)] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 0
        m_size[i][i] = (T[i][0], T[i][1])
    for i in range(n-1):
        dp[i][i+1] = multiply(T[i], T[i+1])
        m_size[i][i+1] = (T[i][0], T[i+1][1])

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            for k in range(i, j):
                if dp[i][j] > dp[i][k] + dp[k+1][j] + multiply(m_size[i][k], m_size[k+1][j]):
                    dp[i][j] = dp[i][k] + dp[k+1][j] + multiply(m_size[i][k], m_size[k+1][j])
                    m_size[i][j] = (m_size[i][k][0], m_size[k+1][j][1])
    return dp[0][n-1]

T = [(5, 4), (4, 6), (6, 2), (2, 7)]
MCM(T)