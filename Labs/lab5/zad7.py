# Zadanie 7. (wydawanie monet) Mamy daną tablicę z nominałami monet stosowanych
# w pewnym dziwnym kraju, oraz kwotę T. Proszę podać algorytm, który oblicza
# minimalną ilość monet potrzebną do wydania kwoty T (algorytm zachłanny, wydający
# najpierw największą monetę, nie działa: dla monet 1, 5, 8 wyda kwotę 15 jako
# 8+5+1+1 zamiast 5+5+5).

def MinimumCoin(price, values):
    dp = [0] + [float('inf')] * price

    for val in range(1, price + 1):
        for coin in values:
            if val - coin >= 0:
                dp[val] = min(dp[val], dp[val - coin] + 1)
    return dp[price]


val = [1, 5, 8]
price = 15
print(MinimumCoin(15, val))