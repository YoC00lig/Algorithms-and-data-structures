"""
Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences.
If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.


"""

def shortestCommonSupersequence(str1,str2):

    def lcs(A, B):
        n = len(A)
        m = len(B)
        dp = [[""] * (m + 1) for _ in range(n + 1)]
        for i in range(n):
            for j in range(m):
                if A[i] == B[j]:
                    dp[i + 1][j + 1] = dp[i][j] + A[i]
                else:
                    dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
        return dp[-1][-1]

    def scs(A, B):
        res, i, j = "", 0, 0
        l = lcs(A, B)
        for c in l:
            while A[i] != c:
                res += A[i]
                i += 1
            while B[j] != c:
                res += B[j]
                j += 1
            res += c
            i += 1
            j += 1
        return res + A[i:] + B[j:]

    return scs(str1, str2)