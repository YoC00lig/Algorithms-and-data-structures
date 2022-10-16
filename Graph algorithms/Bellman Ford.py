def bellman_ford(G, start):
    n = len(G)
    inf = float('inf')
    weights = [inf] * n
    parents = [None] * n
    weights[start] = 0

    for _ in range(n):
        for u in range(n):
            for v, weight in G[u]:
                if weights[u] + weight < weights[v]:
                    weights[v] = weights[u] + weight
                    parents[v] = u

    for _ in range(n): # cykl ujemny
        for u in range(n):
            for v, weight in G[u]:
                if weights[u] + weight < weights[v]: weights[v] = -inf

    return weights, parents


def get_shortest_path(G, s, t):
    weights, parents = bellman_ford(G, s)
    if weights[t] == float('-inf'): return None
    path = []
    while t != s:
        path.append(t)
        t = parents[t]
    path.append(s)
    path.reverse()
    return path