# You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it
# represented by an array nums. You are asked to burst all the balloons.

# If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1
# goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.

# Return the maximum coins you can collect by bursting the balloons wisely.

# Example 1:

# Input: nums = [3,1,5,8]
# Output: 167
# Explanation:
# nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
# coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167

# Example 2:
# Input: nums = [1,5]
# Output: 10

# f(i,j) - maksymalny zysk z pekniec od itego balonika do jtego balonika, uwzgledniajac
# ze miedzy indekssami i, j znajduje sie taki, ktory peka ostatni

def pop_ballons(nums):
    n = len(nums)
    profit = [[0] * n for _ in range(n)]
    for i in range(n):
        profit[i][i] = (nums[i-1] if i != 0 else 1) * nums[i] * (nums[i+1] if i != n-1 else 1)

    for i in range(n-2, -1, -1):
        for j in range(i+1, n):
            for k in range(i, j + 1):
                left = (profit[i][k-1] if k != i else 0)
                p = (nums[i-1] if i-1 >= 0 else 1) * nums[k] * (nums[j+1] if j+1 <= n-1 else 1)
                right = (profit[k+1][j] if k != j else 0)


                if profit[i][j] < (profit[i][k-1] if k != i else 0) + (profit[k+1][j] if k != j else 0) + (nums[i-1] if i-1 >= 0 else 1) * nums[k] * (nums[j+1] if j+1 <= n-1 else 1):
                    profit[i][j] = (profit[i][k-1] if k != i else 0) + (profit[k+1][j] if k != j else 0) + (nums[i-1] if i-1 >= 0 else 1) * nums[k] * (nums[j+1] if j+1 <= n-1 else 1)

    return profit[0][n - 1]
