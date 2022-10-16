# Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

# Input: s1 = "sea", s2 = "eat"
# Output: 231
# Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
# Deleting "t" from "eat" adds 116 to the sum.
# At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

# podejście podobne do longest common subsequence, tylko zamiast najdłuzszego wspólnego
# podciągu szukamy sumy ASCII tego ciągu

def minimumDeleteSum(s1,s2):

    def lcs(X, Y):
        m = len(X)
        n = len(Y)
        sum1 = 0
        for i in X:
            sum1 += ord(i)
        for i in Y:
            sum1 += ord(i)

        L = [[0 for _ in range(n + 1)] for x in range(m + 1)]
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if X[i - 1] == Y[j - 1]:
                    L[i][j] = L[i - 1][j - 1] + ord(X[i - 1])
                else:
                    L[i][j] = max(L[i - 1][j], L[i][j - 1])
        return sum1 - L[m][n] * 2

    return lcs(s1, s2)