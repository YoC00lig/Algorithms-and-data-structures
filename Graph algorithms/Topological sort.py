def TopoSort(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = [-1 for _ in range(n)]
    i = n - 1

    def DFS(u):
        nonlocal visited, result, i
        visited[u] = True
        for v in G[u]:
            if not visited[v]:
                DFS(v)
        result[i] = u
        i -= 1

    for w in range(n):
        if not visited[w]:
            DFS(w)

    return result
