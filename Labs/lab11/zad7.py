# Zadanie 5. (rozłączne ścieżki) Dany jest graf skierowany G = (V,E) oraz wierzchołki s i t. Proszę
# zaproponować algorytm znajdujący maksymalną liczbę rozłącznych (wierzchołkowo) ścieżek między s i t.


# Tworzę nowy graf rozmiaru 2*n, gdzie n to ilosc wierzcholkow w wejsciowym grafie
# jesli w grafie istnieje krawedz z u do v, to w nowym grafie tworze krawedz z u do u+n, z u+n do v+n, z v+n do v
# maksymalny przepływ w tym grafie to ilosc rozlacznych sciezek


def BFS(G, start, end, P):
    n = len(G)
    visited = [False]*n
    q = []
    q.append(start)
    visited[start] = True

    while q:
        u = q.pop(0)
        if u == end: return True
        for i in range(n):
            if not visited[i] and G[u][i] > 0:
                q.append(i)
                visited[i] = True
                P[i] = u

    return False

def FordFulkerson(G, start, end):
    n = len(G)
    P = [-1]*n
    MaxFlow = 0

    while BFS(G, start, end, P):
        path, s, vertex = float("inf"), end, end

        while s != start:
            path = min(path, G[P[s]][s])
            s = P[s]

        MaxFlow += path

        while vertex != start:
            u = P[vertex]
            G[u][vertex] -= path
            G[vertex][u] += path
            vertex = P[vertex]

    return MaxFlow

from math import inf

def DisjointPaths(graph, s, t):
    n = len(graph)
    G = [[0] *(2*n) for _ in range(2*n)]

    for i in range(n):
        for j in range(n):
            if graph[i][j]: G[i+n][j] = 1


    for i in range(n):
        if i == s or i == t: G[i][i+n] = inf
        else: G[i][i+n] = 1


    return FordFulkerson(G, s, t)