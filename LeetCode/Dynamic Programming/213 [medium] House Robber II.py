# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed.
# All houses at this place are arranged in a circle.
# That means the first house is the neighbor of the last one.
# Meanwhile, adjacent houses have a security system connected,
# and it will automatically contact the police if two adjacent houses were broken into on the same night.

# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

# Input: nums = [2,3,2]
# Output: 3
# Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.


def rob(nums):
    n = len(nums)
    if n == 1: return nums[0]
    start = [0] * n
    start[0] = nums[0]
    end = [0] * n
    end[1] = nums[1]

    for i in range(1, n - 1):
        if i - 2 >= 0:
            start[i] = max(start[i - 2] + nums[i], start[i - 1])
        else:
            start[i] = max(nums[i], start[i - 1])

    for i in range(2, n):
        if i - 2 >= 0:
            end[i] = max(end[i - 2] + nums[i], end[i - 1])
        else:
            end[i] = max(nums[i], end[i - 1])

    return max(end[-1], start[n - 2])
