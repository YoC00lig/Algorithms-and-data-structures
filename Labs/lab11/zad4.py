# Zadanie 2. (spójność krawędziowa) Dany jest graf nieskierowany G = (V,E). Mówimy, że spójność
# krawędziowa G wynosi k jeśli usunięcie pewnych k krawędzi powoduje, że G jest niespójny, ale
# usunięcie dowolnych k − 1 krawędzi nie rozspójnia go. Proszę podać algorytm, który oblicza spójność
# krawędziową danego grafu.

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

# wybieram jeden wierzchołek który będzie źródłem i dla niego szukam kolejnego wierzchołka dla
# którego przepływ bedzie minimalny

def EdgeConsistency(G):
    n, u, result = len(G), 0, inf
    for v in range(1,n): result = min(result, FordFulkerson(G, u, v))
    return result
