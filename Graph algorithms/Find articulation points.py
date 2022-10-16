def find_articulation_points(G):
    n = len(G)
    low = [0] * n
    ids = [0] * n
    is_art = [False] * n
    id = 0
    out_deg = 0

    def dfs(root, u, parent):
        nonlocal id, out_deg
        if parent == root: out_deg += 1
        id += 1
        low[u] = ids[u] = id

        for v in G[u]:
            if v == parent: continue
            if not ids[v]:
                dfs(root, v, u)
                low[u] = min(low[u], low[v])
                if ids[u] <= low[v]: is_art[u] = True
            else: low[u] = min(low[u], ids[v])

    for u in range(n):
        if not ids[u]:
            out_deg = 0
            dfs(u, u, -1)
            is_art[u] = out_deg > 1

    return [u for u in range(n) if is_art[u]]