def CoherentComponents(G):
    n = len(G)
    result = []
    visited = [False] * n

    def DFS(u):
        visited[u] = True
        for v, _ in G[u]:
            if not visited[v]:
                DFS(v)

    for u in range(n):
        if not visited[u]:
            result.append(u)
            DFS(u)
    return result