"""
You are given a 2D array of integers envelopes where envelopes[i] = [wi, hi] represents the width and the height of an envelope.

One envelope can fit into another if and only if both the width and height of one envelope are greater than the other envelope's width and height.

Return the maximum number of envelopes you can Russian doll (i.e., put one inside the other).

Note: You cannot rotate an envelope.
"""


def maxEnvelopes(envelopes):
    def Binsearch(T, val, start, end):
        n = len(T)
        left, right = start, end
        while left <= right:
            mid = (left + right) // 2
            if T[mid] == val:
                return mid
            elif T[mid] < val:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def LIS(T):
        lenght = 1
        n = len(T)
        res = [0] * n
        res[0] = T[0][1]

        for i in range(1, n):
            if T[i][1] > res[lenght - 1]:
                res[lenght] = T[i][1]
                lenght += 1
            elif T[i][1] < res[0]:
                res[0] = T[i][1]
            else:
                index = Binsearch(res, T[i][1], 0, lenght - 1)
                res[index] = T[i][1]
        return lenght

    envelopes.sort(key=lambda x: (x[0], -x[1]))
    return LIS(envelopes)