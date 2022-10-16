# Zadanie 1. (maksymalny przepływ w grafie nieskierowanym) Proszę wskazać algorytm, który znaj-
# duje maksymalny przepływ między źródłem i ujściem w grafie nieskierowanym. Proszę użyć algorytmu
# z wykładu — dla grafów skierowanych, gdzie między każdą parą wierzchołków jest najwyżej jedna
# krawędź — jako czarnej skrzynki. Alternatywnie można opisać implementację bezpośrednio pracującą
# na grafie nieskierowanym.

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


def UndirectedMF(graph, s, t):
    n = len(graph)
    edges_num = 0

    for i in range(n):
        for j in range(i+1, n):
            if graph[i][j] > 0: edges_num += 1

    m = edges_num + n
    G = [[0]*m for _ in range(m)]
    new_vert = n

    for u in range(n):
        for v in range(u+1,n):
            if graph[u][v] > 0:
                G[u][v] = graph[u][v]
                G[v][new_vert] = G[new_vert][u] = graph[u][v]
                new_vert += 1

    return FordFulkerson(G, s, t)


