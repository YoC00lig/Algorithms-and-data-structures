from queue import PriorityQueue

# matrix O(V^2)
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

# adjacency list O(ElogV)

def Dijkstra2_(G, start):
    n = len(G)
    D = [float("inf")]*n
    P = [None] * n
    Q = PriorityQueue()

    Q.put((0, start))
    D[start] = 0
    while not Q.empty():
        minD, u = Q.get()
        for v, dist in G[u]:
            if D[v] > D[u] + dist:
                D[v] = D[u] + dist
                P[v] = u
                Q.put((D[v], v))

    return D
