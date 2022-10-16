# You are given an integer array coins representing coins of different
# denominations and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. If that amount
# of money cannot be made up by any combination of the coins, return 0.
# You may assume that you have an infinite number of each kind of coin.
# The answer is guaranteed to fit into a signed 32-bit integer.

# Input: amount = 5, coins = [1,2,5]
# Output: 4
# Explanation: there are four ways to make up the amount:
# 5=5
# 5=2+2+1
# 5=2+1+1+1
# 5=1+1+1+1+1

# SOLUTION
# how many combinations of a given value can I make by adding another coin?

# Value:     0 | 1 | 2 | 3 | 4 | 5
# start      1 | 0 | 0 | 0 | 0 | 0
# coin:  1   1 | 1 | 1 | 1 | 1 | 1
# coin:  2   1 | 1 | 2 | 2 | 3 | 3
# coin:  5   1 | 1 | 2 | 2 | 3 | 4

def change(amount, coins):
    dp = [0] * (amount + 1)
    dp[0] = 1

    for coin in coins:
        for price in range(coin, amount + 1):
            dp[price] += dp[price - coin]

    return dp[-1]