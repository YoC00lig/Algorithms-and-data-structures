# Zadanie 1. (DFS/BFS) Proszę zaimplementować następujące algorytmy:
# 1. Sprawdzanie czy graf jest dwudzielny (czyli zauważyć, że to 2-kolorowanie i użyć DFS lub BFS).

def CheckIfIsBipartite(G):
    n = len(G)
    colors = [0] * n

    def DFS(u):
        for v in G[u]:
            if not colors[v]: # jeśli nie został odwiedzony to ma 0
                colors[v] = 3 - colors[u]
                if not DFS(v): return False
            elif colors[v] == colors[u]:
                return False

        return True

    for u in range(n):
        if not colors[u]:
            colors[u] = 1 # ustawiam pierwszy kolor
            if not DFS(u): return False

    return True


# 2. Policzyć liczbę spójnych składowych w grafie (implementacja przeciwna do tej z poprzedniego zadania)

def NO_connected_components(G):
    n = len(G)
    visited = [False] * n

    def DFS(u):
        visited[u] = True
        for v in G[u]:
            if not visited[v]: DFS(v)

    cnt = 0
    for u in range(n):
        if not visited[u]:
            cnt += 1
            DFS(u)

    return cnt