# You are given a string s.
# A split is called good if you can split s into two
# non-empty strings sleft and sright where their concatenation
# is equal to s (i.e., sleft + sright = s) and the number of distinct
# letters in sleft and sright is the same.
# Return the number of good splits you can make in s.

def numSplits(s):
    n = len(s)
    prefix = [0] * n
    sufix = [0] * n
    tab = [0] * 27
    unique = 0

    for i in range(n):
        index = ord(s[i]) - 97
        tab[index] += 1
        if tab[index] == 1:
            unique += 1
        prefix[i] = unique

    tab = [0] * 27
    unique = 0
    for i in range(n - 1, -1, -1):
        index = ord(s[i]) - 97
        tab[index] += 1
        if tab[index] == 1:
            unique += 1
        sufix[i] = unique

    cnt = 0
    for i in range(len(prefix) - 1):
        if prefix[i] == sufix[i + 1]:
            cnt += 1
    return cnt