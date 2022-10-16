"""
Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example,
the array nums = [0,1,4,4,5,6,7] might become:

[4,5,6,7,0,1,4] if it was rotated 4 times.
[0,1,4,4,5,6,7] if it was rotated 7 times.
Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the
 array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

Given the sorted rotated array nums that may contain duplicates, return the minimum element of this array.

You must decrease the overall operation steps as much as possible.
"""

def findMin(nums):
    left = 0
    right = len(nums) - 1
    if len(nums) == 1:
        return nums[0]
    if nums[0] < nums[right]:
        return nums[0]
    if len(set(nums)) == 1:
        return nums[0]

    while left < right:
        mid = (left + right) // 2
        while left + 1 < len(nums) and nums[left] == nums[left + 1]:
            left += 1
        if left == len(nums):
            return None
        while right >= 0 and nums[right] == nums[right - 1]:
            right -= 1
        if right < 0:
            return None
        if nums[mid] > nums[mid + 1]:
            return nums[mid + 1]
        elif nums[mid] < nums[left]:
            right = mid
        elif nums[mid] > nums[right]:
            left = mid