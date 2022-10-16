# Given an array of non-negative integers nums, you are initially positioned at the first index of the array.
# Each element in the array represents your maximum jump length at that position.
# our goal is to reach the last index in the minimum number of jumps.
# You can assume that you can always reach the last index.

# Input: nums = [2,3,1,1,4]
# Output: 2
# Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step
# from index 0 to 1, then 3 steps to the last index.

def jump(nums):
    n = len(nums)
    tab = [float('inf')] * n
    tab[0] = 0
    for i in range(n):
        jump = nums[i]
        for j in range(i + 1, i + jump + 1):
            if j > n - 1:
                break
            else:
                tab[j] = min(tab[j], tab[i] + 1)
                if j == n - 1: return tab[j]
    print(tab)
    return tab[-1]