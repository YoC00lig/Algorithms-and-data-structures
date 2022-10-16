# You are a professional robber planning to rob houses along a street.
# Each house has a certain amount of money stashed, the only constraint s
# topping you from robbing each of them is that adjacent houses have security
# systems connected and it will automatically contact the police if two adjacent
# houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house,
# return the maximum amount of money you can rob tonight without alerting the police.

#Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.

def rob(nums):
    n = len(nums)
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(1, n):
        if i - 2 >= 0:
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        else:
            dp[i] = max(nums[i], dp[i - 1])
    return dp[-1]