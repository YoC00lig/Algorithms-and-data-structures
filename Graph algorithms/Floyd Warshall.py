from math import inf

def FloydWarshall(G, start, end):
    n = len(G)
    W = [[inf] * n for _ in range(n)]
    P = [[None] * n for _ in range(n)] # parents

    for i in range(n):
        for j in range(n):
            if G[i][j] != 0:
                W[i][j] = G[i][j]
                P[i][j] = j

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]:
                    W[i][j] = W[i][t] + W[t][j]
                    P[i][j] = P[i][t]

    for t in range(n):
        for i in range(n):
            for j in range(n):
                if W[i][t] + W[t][j] < W[i][j]: # ujemny cykl
                    W[i][j] = -inf
                    P[i][j] = None

    if P[start][end] is None: return [] # odtwarzanie ścieżki
    path = [start]
    while start != end:
        start = P[start][end]
        path.append(start)

    return W, P, path