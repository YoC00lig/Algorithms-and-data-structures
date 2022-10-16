"""
You may recall that an array arr is a mountain array if and only if:

arr.length >= 3
There exists some index i (0-indexed) with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Given an integer array nums, return the minimum number of elements to remove to
make nums a mountain array.


"""


def minimumMountainRemovals(nums):
    def Binsearch(T, val, start, end):
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2
            if T[mid] > val:
                right = mid - 1
            else:
                left = mid + 1
        return left

    def LIS(T):
        n = len(T)
        res = [0] * n
        res[0] = T[0]
        dp = [0] * n
        dp[0] = 0
        lenght = 1

        for i in range(1, n):
            if T[i] > res[lenght - 1]:
                res[lenght] = T[i]
                lenght += 1
            elif T[i] < res[0]:
                res[0] = T[i]
            else:
                index = Binsearch(res, T[i], 0, lenght - 1)
                res[index] = T[i]

            dp[i] = i + 1 - lenght if i + 1 - lenght != i else float("inf")

        return dp

    inc = LIS(nums)
    nums.reverse()
    dec = LIS(nums)
    dec.reverse()

    mini = float("inf")

    for i in range(1, len(inc) - 1):
        mini = min(mini, inc[i] + dec[i])
        mini = min(mini, dec[i] + inc[i])
    return mini