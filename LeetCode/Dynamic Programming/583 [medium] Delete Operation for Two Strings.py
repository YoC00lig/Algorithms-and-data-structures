# Given two strings word1 and word2, return the minimum number of steps
# required to make word1 and word2 the same.
# In one step, you can delete exactly one character in either string.

#Input: word1 = "sea", word2 = "eat"
# Output: 2
# Explanation: You need one step to make "sea" to "ea" and
# another step to make "eat" to "ea".

# Longest common subsequence and return number of letters that are not contained at result

def minDistance(word1,word2):

    def lms(arr1, arr2):
        n = len(arr1)
        m = len(arr2)
        func = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if arr1[i - 1] == arr2[j - 1]:
                    func[i][j] = func[i - 1][j - 1] + 1
                else:
                    func[i][j] = max(func[i - 1][j], func[i][j - 1])
        return func[n][m]

    same = lms(word1, word2)
    n, m = len(word1), len(word2)
    result = n - same + m - same
    return result