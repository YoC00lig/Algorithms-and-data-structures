# Zadanie 1. (problem plecakowy) Proszę podać i zaimplementować algorytm znajdujący
# wartość optymalnego zbioru przedmiotów w dyskretnym problemie plecakowym. Algorytm
# powinien działać w czasie wielomianowym względem liczby przedmiotów oraz sumy ich profitów.

# STANDARDOWY PROBLEM PLECAKOWY
# złożoność czasowa O(n*w),
# gdzie n to liczba przedmiotów i w to maksymalna pojemność plecaka

weights = [2, 2, 3, 15,1,4,5,6]
profits = [40,160,70,300,70,25,25,180]
capacity = 15

def KnapSack1(weights, profit, capacity):
    matrix = [[0 for _ in range(capacity+1)] for _ in range(len(profit))]
    for w in range(capacity+1):
        if weights[0] <= w:
            matrix[0][w] = profit[0]

    for n in range(1,len(profit)):
        for w in range(1,capacity+1):
            if w >= weights[n]:
                matrix[n][w] = max(matrix[n-1][w], matrix[n-1][w-weights[n]] + profit[n])
            else:
                matrix[n][w] = matrix[n-1][w]
    print(GetSolution1(matrix,profits,weights,len(profits)-1,capacity))
    return matrix[-1][-1]

def GetSolution1(m,profits,weights,curritem,currmaxw):
    if curritem == 0:
        if weights[curritem] <= currmaxw: return [curritem]
        else: return []

    if currmaxw - weights[curritem] >= 0:
        if m[curritem][currmaxw] == m[curritem-1][currmaxw - weights[curritem]] + profits[curritem]:
            return GetSolution1(m,profits,weights,curritem-1,currmaxw - weights[curritem]) + [curritem]
    return GetSolution1(m,profits,weights,curritem-1,currmaxw)

print(KnapSack1(weights,profits,capacity))

# KNAPSACK WZGLĘDEM PRZEDMIOTÓW I SUMY PROFITÓW
# O(n*sum(profits))
#  f(i, p) - min weight of things from indexes 0 to i, having
#            summary profit equal or greater than p

def KnapSack2(weights, profits, capacity):
    matrix = [[float('inf') for _ in range(sum(profits)+1)] for _ in range(len(profits))]

    for i in range(profits[0] + 1):
        matrix[0][i] = weights[0]

    for item in range(1,len(profits)):
        for profit in range(sum(profits)+1):
            if profits[item] - profit >= 0:
                matrix[item][profit] = min(weights[item], matrix[item-1][profit])
            else: matrix[item][profit] = matrix[item-1][profit]
            if profit - profits[item] >= 0:
                matrix[item][profit] = min(matrix[item][profit], matrix[item-1][profit-profits[item]] + weights[item])

    for i in range(sum(profits),-1,-1):
        if matrix[len(profits)-1][i] <= capacity:
            print(GetSolution2(matrix, profits, weights, len(profits) - 1, i))
            return i

def GetSolution2(m,profits,weights,item,profit):
    if item == 0:
        if profit >= profits[0]:
            return [item]
        return []
    if profit-profits[item] >= 0 and (m[item][profit] == m[item-1][profit-profits[item]] + weights[item] or m[item][profit]==weights[item] ):
        return GetSolution2(m,profits,weights,item-1,profit-profits[item]) + [item]
    else:
        return GetSolution2(m,profits,weights,item-1,profit)

print(KnapSack2(weights,profits,capacity))
