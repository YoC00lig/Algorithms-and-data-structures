# 1.Wykonaj DFS dla grafu wejściowego zapisując w wierzchołkach czasy przetworzenia
# 2.Odwróć kolejność krawędzi
# 3.Wykonaj DFS drugi raz

def scc(G):
    n = len(G)
    visited = [False]*n
    time = 0
    vwt = []

    def dfstime(u):
        nonlocal time, visited, vwt
        visited[u] = True
        for v in G[u]:
            if not visited[v]: dfstime(v)
        time += 1
        vwt.append([u, time])

    for u in range(n):
        if not visited[u]: dfstime(u)

    vwt.reverse()
    reversed = [[] for _ in range(n)]

    for u in range(n):
        for neigh in G[u]: reversed[neigh].append(u)

    result = []
    cnt = 0
    visited = [False]*n

    def dfs(u, cnt):
        nonlocal result, visited
        result[cnt].append(u)
        visited[u] = True
        for v in reversed[u]:
            if not visited[v]: dfs(v,cnt)

    for u,_ in vwt:
        if not visited[u]:
            result.append([])
            dfs(u, cnt)
            cnt += 1

    return result