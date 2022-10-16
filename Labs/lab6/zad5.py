# Zadanie 5 (dwuwymiarowy problem plecakowy) Proszę zaproponować algorytm dla
# dwuwymiarowej wersji dyskretnego problemu plecakowego. Mamy dany zbiór
# P = {p1,...,pn} przedmiotów i dla każdego przedmiotu pi dane sa nastepujace trzy liczby:

# 1. v(pi) – wartość przedmiotu,
# 2. w(pi) – waga przedmiotu, oraz 3. h(pi) – wysokość przedmiotu.

# Złodziej chce wybrać przedmioty o maksymalnej wartości, których łączna waga
# nie przekracza danej liczby W oraz których łączna wysokość nie przekracza
# danej liczby H (przedmioty zapakowane są w kartony, które złodziej układa jeden na drugim).
# Proszę oszacować złozoność czasową swojego algorytmu oraz uzasadnić jego poprawność.

#f(i,h,w) - profit jaki możemy osiągnąć do elementu od 0 do i włącznie, mając maksymalną wyskość h i wagę w

def GetSolution(dp,weights,heights,profits,maxW,maxH):
    def rec(el,h,w):
        if el < 0: return []
        if el == 0:
            if h >= heights[0] and w>= weights[0]: return [0]
            else: return []
        if h >= heights[el] and w >= weights[el] and dp[el][h][w] == dp[el-1][h-heights[el]][w-weights[el]] + profits[el]:
            return rec(el-1,h-heights[el],w - weights[el]) + [el]
        return rec(el-1, h, w)
    return rec(len(weights)-1, maxH, maxW)

def knapsack_2D(profits, weights, heights, maxW, maxH):
    n = len(profits)
    dp = [[[0 for _ in range(maxH+1)] for _ in range(maxW+1)] for _ in range(n)]

    for height in range(heights[0],maxH+1):
        for weight in range(weights[0],maxW+1):
            dp[0][height][weight] = profits[0]

    for el in range(1,n):
        for h in range(1,maxH+1):
            for w in range(1,maxW+1):
                dp[el][h][w] = dp[el-1][h][w]
                if heights[el] <= h and weights[el] <= w:
                    dp[el][h][w] = max(dp[el][h][w], dp[el-1][h-heights[el]][w-weights[el]] + profits[el])

    return dp[n-1][maxH][maxW]

