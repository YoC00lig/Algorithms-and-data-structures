"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.
"""

def minCut(s):
    n = len(s)
    P = [[False] * n for _ in range(n)]
    C = [0] * (n + 1)

    for i in range(n):
        P[i][i] = True

    for L in range(2, n + 1):
        for i in range(n - L + 1):
            j = i + L - 1
            if L == 2:
                P[i][j] = True if s[i] == s[j] else False
            else:
                P[i][j] = True if (s[i] == s[j] and P[i + 1][j - 1]) else False

    for i in range(n):
        if P[0][i]: C[i] = 0
        else:
            C[i] = float("inf")
            for j in range(i):
                if P[j + 1][i] and 1 + C[j] < C[i]:
                    C[i] = C[j] + 1

    return C[n - 1]