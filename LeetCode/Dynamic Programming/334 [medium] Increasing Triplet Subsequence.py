# Given an integer array nums, return true if there exists a triple of indices
# (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.

def increasingTriplet1(nums):
    def BinarySearch(T, number, start, end):
        left = start
        right = end
        while left <= right:
            mid = (left + right) // 2
            if T[mid] == number:
                return mid
            elif T[mid] < number:
                left = mid + 1
            else:
                right = mid - 1
        return left

    def LongIncSub1(T):
        lenght = 1
        n = len(T)
        result = [0 for _ in range(n)]
        result[0] = T[0]
        for i in range(1, n):
            if T[i] > result[lenght - 1]:
                result[lenght] = T[i]
                lenght += 1
                if lenght == 3: return True
            elif T[i] < result[0]:
                result[0] = T[i]
            else:
                index = BinarySearch(result, T[i], 0, lenght - 1)
                result[index] = T[i]
        return False

    return LongIncSub1(nums)

# O (n)
def increasingTriplet2(nums):
    first = second = float('inf')
    for number in nums:
        if number <= first: first = number
        elif number <= second: second = number
        else: return True
    return False