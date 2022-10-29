from kol3atesty import runtests
from queue import PriorityQueue

def Dijkstra(G,s,t):
    n = len(G)
    q = PriorityQueue()
    dist = [float("inf")]*n
    dist[s] = 0
    q.put((0, s))

    while not q.empty():
        distance, u = q.get()
        if u == t: break

        for v, time in G[u]:
            if dist[v] > dist[u] + time:
                dist[v] = dist[u] + time
                q.put((dist[v], v))

    return dist[t] if dist[t] != float("inf") else None

def spacetravel( n, E, S, a, b ):
    G = [[] for _ in range(n+1)]

    for u,v,time in E:
        G[u].append([v, time])
        G[v].append([u, time])

    for u in S:
        G[n].append([u, 0])
        G[u].append([n, 0])

    return Dijkstra(G, a, b)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True)