#Given a string s, return the number of palindromic substrings in it.
# A string is a palindrome when it reads the same backward as forward.
# A substring is a contiguous sequence of characters within the string.

def countSubstrings(s):
    ans = 0
    n = len(s)

    for i in range(n):
        left, right = i, i

        while left >= 0 and right < n and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1

        left, right = i, i + 1
        while left >= 0 and right < n and s[left] == s[right]:
            ans += 1
            left -= 1
            right += 1
    return ans