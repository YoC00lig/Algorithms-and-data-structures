"""
Given an array nums which consists of non-negative integers and an integer m, you can split the array
into m non-empty continuous subarrays.

Write an algorithm to minimize the largest sum among these m subarrays.

"""

def splitArray(nums,m):
    n = len(nums)

    # funkcja sprawdza na ile tablic trzeba by było podzielić główną tablicę tak,
    # by maksymalna suma jaka jest w każdej z tych tablic była maksymalnie równa x
    def SplitToSum(x):
        suma = 0
        splits = 0
        for i in range(n):
            if suma + nums[i] <= x:
                suma += nums[i]
            else:
                splits += 1
                suma = nums[i]
        return splits + 1
    # binsearch
    left = max(nums)
    right = sum(nums)
    mini = 0
    while left <= right:
        mid = (left + right) // 2
        if SplitToSum(mid) <= m:
            right = mid - 1
            mini = mid
        elif SplitToSum(mid) > m:
            left = mid + 1

    return mini