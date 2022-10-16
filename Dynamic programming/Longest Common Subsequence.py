def lcs(A,B):
    n = len(A)
    m = len(B)
    dp = [[""] * (m+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                dp[i+1][j+1] = dp[i][j] + A[i]
            else:
                dp[i+1][j+1] = max(dp[i+1][j], dp[i][j+1], key = len)
    return dp[-1][-1]