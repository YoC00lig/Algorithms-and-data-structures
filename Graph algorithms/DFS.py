def DFS(G, start):
    n = len(G)
    visited = [False] * n

    def rec(u):
        nonlocal visited
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                rec(v)

    rec(start)