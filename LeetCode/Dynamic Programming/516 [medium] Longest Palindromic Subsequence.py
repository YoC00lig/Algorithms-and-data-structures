# Given a string s, find the longest palindromic subsequence's length in s.
# A subsequence is a sequence that can be derived from another sequence by
# deleting some or no elements without changing the order of the remaining elements.


# just longest common subsequence at s and reversed s

def longestPalindromeSubseq(s):
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

    v = s[::-1]
    return lms(s, v)
