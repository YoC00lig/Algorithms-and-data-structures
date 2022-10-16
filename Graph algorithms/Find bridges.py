def findbridges(G):
    n = len(G)
    low = [0] * n
    times = [0] * n
    bridges = []
    time = 0

    def dfs(u, parent):
        nonlocal time
        time += 1
        low[u] = times[u] = time

        for v in G[u]:
            if v == parent: continue
            if not times[v]:
                dfs(v, u)
                if low[v] < low[u]: low[u] = low[v]
            else: low[u] = min(low[u], times[v])

        if times[u] == low[u] and parent >= 0: bridges.append((parent, u))

    for i in range(n):
        if not times[i]:
            dfs(i, -1)

    return bridges