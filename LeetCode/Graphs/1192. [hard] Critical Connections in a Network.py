"""
There are n servers numbered from 0 to n - 1 connected by undirected server-to-server connections forming a network where connections[i] = [ai, bi] represents a connection between servers ai and bi. Any server can reach other servers directly or indirectly through the network.

A critical connection is a connection that, if removed, will make some servers unable to reach some other server.

Return all critical connections in the network in any order.


"""


def criticalConnections(n, connections):
    G = [[] for _ in range(n)]
    for u, v in connections:
        G[u].append(v)
        G[v].append(u)

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
                if parent == v: continue
                if not times[v]:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])

                else:
                    low[u] = min(low[u], times[v])


            if times[u] == low[u] and parent >= 0:
                bridges.append((parent, u))

        for i in range(n):
            if not times[i]:
                dfs(i, -1)

        return bridges

    return findbridges(G)