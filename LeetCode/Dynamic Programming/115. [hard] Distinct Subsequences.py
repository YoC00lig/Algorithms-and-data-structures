"""
Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

The test cases are generated so that the answer fits on a 32-bit signed integer.
"""


def numDistinct(s,t):
    longer = len(s)
    shorter = len(t)

    dp = [[0] * (longer + 1) for _ in range(shorter + 1)]

    for i in range(longer + 1):
        dp[0][i] = 1

    for si in range(1, longer + 1):
        for ti in range(1, shorter + 1):
            if s[si - 1] != t[ti - 1]:
                dp[ti][si] = dp[ti][si - 1]
            else:
                dp[ti][si] = dp[ti][si - 1] + dp[ti - 1][si - 1]

    return dp[shorter][longer]