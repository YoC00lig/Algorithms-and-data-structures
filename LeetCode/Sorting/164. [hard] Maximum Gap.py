"""
Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.

"""


def maximumGap(nums):
    if len(nums) < 2: return 0
    n, mini, maxi = len(nums), min(nums), max(nums)
    interval = (maxi - mini) / n
    if interval == 0: return 0
    buckets = [[] for _ in range(n)]

    for val in nums:
        index = int((val - mini) / interval) if int((val - mini) / interval) < n else n - 1
        buckets[index].append(val)

    first = None
    for i in range(n):
        if buckets[i] != []:
            first = i
            break

    result = 0
    for i in range(first + 1, n):
        if buckets[i] != []:
            result = max(result, min(buckets[i]) - max(buckets[first]))
            first = i
    return result