# Zadanie 4. (malejące krawędzie) Dany jest graf G = (V, E), gdzie każda krawędź ma wagę
# ze zbioru {1, . . . , ∣E∣} (wagi krawędzi są parami różne). Proszę zaproponować algorytm,
# który dla danych wierzchołków x i y sprawdza, czy istnieje ścieżka z x do y, w której
# przechodzimy po krawędziach o coraz mniejszych wagach.


def DecreasingEdges(G,x,y):
    n = len(G)
    visited = [[False]*n for _ in range(n)]

    def dfs(u, val):
        if u == y: return True
        for v in range(n):
            if not visited[u][v] and G[u][v] < val:
                visited[u][v] = visited[v][u] = True
                if dfs(v, G[u][v]): return True
        return False

    for u in range(n):
        if not visited[x][u]:
            visited[x][u] = visited[u][x] = True
            if dfs(u, G[x][u]): return True

    return False