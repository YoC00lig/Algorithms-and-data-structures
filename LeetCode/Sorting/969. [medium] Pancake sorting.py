"""
Given an array of integers arr, sort the array by performing a series of pancake flips.

In one pancake flip we do the following steps:

Choose an integer k where 1 <= k <= arr.length.
Reverse the sub-array arr[0...k-1] (0-indexed).
For example, if arr = [3,2,1,4] and we performed a pancake flip choosing k = 3, we reverse
the sub-array [3,2,1], so arr = [1,2,3,4] after the pancake flip at k = 3.

Return an array of the k-values corresponding to a sequence of pancake flips that sort arr.
 Any valid answer that sorts the array within 10 * arr.length flips will be judged as correct.
"""

def pancakeSort(arr):
    def ifsorted(arr):
        flag = True
        n = len(arr)
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                flag = False
        if flag:
            return True
        return False

    def flip(arr, k):
        cnt = 0
        a = k
        while cnt < a:
            arr[cnt], arr[a] = arr[a], arr[cnt]
            cnt += 1
            a -= 1

    def findmax(arr, last):
        ind = 0
        for i in range(last):
            if arr[i] > arr[ind]:
                ind = i
        return ind

    if ifsorted(arr):
        return []

    res = []
    indinsert = len(arr)
    while indinsert > 0:
        index = findmax(arr, indinsert)
        if index != indinsert - 1:
            if index != 0:
                res.append(index + 1)
                flip(arr, index)
            res.append(indinsert)
            flip(arr, indinsert - 1)
        indinsert -= 1
    return res