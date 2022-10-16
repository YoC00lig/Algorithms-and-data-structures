"""
You are given a 0-indexed array arr consisting of n positive integers, and a positive integer k.

The array arr is called K-increasing if arr[i-k] <= arr[i] holds for every index i, where k <= i <= n-1.

For example, arr = [4, 1, 5, 2, 6, 2] is K-increasing for k = 2 because:
arr[0] <= arr[2] (4 <= 5)
arr[1] <= arr[3] (1 <= 2)
arr[2] <= arr[4] (5 <= 6)
arr[3] <= arr[5] (2 <= 2)
However, the same arr is not K-increasing for k = 1 (because arr[0] > arr[1]) or k = 3 (because arr[0] > arr[3]).
In one operation, you can choose an index i and change arr[i] into any positive integer.

Return the minimum number of operations required to make the array K-increasing for the given k.

"""


def kIncreasing(arr,k):
    def BinSearch(T, val, start, end):
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
        lenght = 1

        for i in range(1, n):
            if T[i] >= res[lenght - 1]:
                res[lenght] = T[i]
                lenght += 1
            elif T[i] < res[0]:
                res[0] = T[i]
            else:
                index = BinSearch(res, T[i], 0, lenght - 1)
                res[index] = T[i]
        return n - lenght

    groups = [[] for _ in range(k)]

    n = len(arr)
    for i in range(n):
        groups[i % k].append(arr[i])

    result = 0
    for group in groups:
        result += LIS(group)
    return result