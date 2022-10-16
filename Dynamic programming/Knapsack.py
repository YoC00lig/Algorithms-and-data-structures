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
    return matrix[-1][-1]

def GetSolution1(m,profits,weights,curritem,currmaxw):
    if curritem == 0:
        if weights[curritem] <= currmaxw: return [curritem]
        else: return []

    if currmaxw - weights[curritem] >= 0:
        if m[curritem][currmaxw] == m[curritem-1][currmaxw - weights[curritem]] + profits[curritem]:
            return GetSolution1(m,profits,weights,curritem-1,currmaxw - weights[curritem]) + [curritem]
    return GetSolution1(m,profits,weights,curritem-1,currmaxw)