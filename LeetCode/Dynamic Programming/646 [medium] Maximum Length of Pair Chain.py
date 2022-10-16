# You are given an array of n pairs pairs where pairs[i] = [lefti, righti] and lefti < righti.
# A pair p2 = [c, d] follows a pair p1 = [a, b] if b < c. A chain of pairs can be formed in this fashion.
# Return the length longest chain which can be formed.
# You do not need to use up all the given intervals. You can select pairs in any order.

# Input: pairs = [[1,2],[2,3],[3,4]]
# Output: 2
# Explanation: The longest chain is [1,2] -> [3,4].

def findLongestChainGREEDY(pairs):
    intervals = pairs
    intervals2 = sorted(intervals, key=lambda x: x[1])
    end = -float('inf')
    count = 0

    for x, y in intervals2:
        if x > end:
            end = y
            count += 1

    return count

def findLongestChainDP(pairs):
    intervals = pairs
    pairs.sort(key=lambda x: x[1])
    dp = [1] * len(intervals)

    for i in range(len(intervals)):
        for j in range(i):
            if intervals[i][0] > intervals[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)
