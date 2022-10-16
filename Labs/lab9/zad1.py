# Zadanie 1. Proszę zaimplementować algorytm Dijkstry (dla wybranej przez prowadzącego reprezentacji grafu).

from queue import PriorityQueue
# macierze O(V^2logV)

def Dijkstra1(G, start):
    n = len(G)
    parents = [None] * n
    dist = [float("inf")] * n
    Q = PriorityQueue()

    Q.put(start)
    dist[start] = 0
    while not Q.empty():
        u = Q.get()
        for v in range(n):
            if G[v][u] != 0:
                if dist[v] > dist[u] + G[u][v]:
                    dist[v] = dist[u] + G[u][v]
                    parents[v] = u
                    Q.put(v)
    return dist

#O(V^2):
def getmin(dist, visited):
    mini = float("inf")
    idx = 0
    for u in range(len(dist)):
        if dist[u] < mini and not visited[u]:
            mini = dist[u]
            idx = u

    return idx

def dijkstra(G, start, end):
    n = len(G)
    dist = [float("inf")] * n
    dist[start] = 0
    visited = [False] * n

    for cnt in range(n):
        x = getmin(dist, visited)
        visited[x] = True
        for y in range(n):
            if G[x][y] > 0 and visited[y] == False and dist[y] > dist[x] + G[x][y]:
                dist[y] = dist[x] + G[x][y]
    return dist[end]

# lista sąsiedztwa
def Dijkstra2(G, start):
    n = len(G)
    P = [None] * n
    D = [float("inf")]*n
    Q = PriorityQueue()

    Q.put(start)
    D[start] = 0
    while not Q.empty():
        u = Q.get()
        for v in G[u]:
            if D[v[0]] > D[u] + v[1]:
                D[v[0]] = D[u] + v[1]
                P[v[0]] = u
                Q.put(v[0])

    return D

G = [[[2,4],[1,1],[3,8]],
     [[0,1],[3,2]],
     [[0,4],[3,2]],
     [[0,8],[1,2],[2,2]]]

