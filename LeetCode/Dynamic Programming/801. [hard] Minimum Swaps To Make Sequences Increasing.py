"""
You are given two integer arrays of the same length nums1 and nums2. In one operation, you are allowed to swap nums1[i] with nums2[i].

For example, if nums1 = [1,2,3,8], and nums2 = [5,6,7,4], you can swap the element at i = 3 to obtain nums1 = [1,2,3,4] and nums2 = [5,6,7,8].
Return the minimum number of needed operations to make nums1 and nums2 strictly increasing. The test cases are generated so that the given input always makes it possible.

An array arr is strictly increasing if and only if arr[0] < arr[1] < arr[2] < ... < arr[arr.length - 1].

"""


def minSwap(A, B):
    dp = [[float('inf'), float('inf')] for i in range(len(A))]  # [NotSwapped, Swapped]

    dp[0][0] = 0
    dp[0][1] = 1

    for i in range(1, len(dp)):
        if A[i] > A[i - 1] and B[i] > B[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][0])

        if A[i] > B[i - 1] and B[i] > A[i - 1]:
            dp[i][0] = min(dp[i][0], dp[i - 1][1])

        if B[i] > A[i - 1] and A[i] > B[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][0] + 1)

        if B[i] > B[i - 1] and A[i] > A[i - 1]:
            dp[i][1] = min(dp[i][1], dp[i - 1][1] + 1)

    return min(dp[-1])