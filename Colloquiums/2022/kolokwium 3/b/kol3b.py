from kol3btesty import runtests
from queue import PriorityQueue

# tworzę nowy wierzchołek, jest to taka "przestrzeń powietrzna", do której będą prowadzić krawędzie, których
# waga to cena przelotu na dane lotnisko.
# Na tak powstałym grafie puszczam algorytm Dijkstry

def Dijkstra(G,s,t):
    n = len(G)
    pq = PriorityQueue()
    D = [float("inf")]*n
    D[s] = 0

    pq.put((0, s))
    while not pq.empty():
        dist, u = pq.get()
        if u == t: break
        for v, cost in G[u]:
            if D[v] > D[u] + cost:
                D[v] = D[u] + cost
                pq.put((D[v], v))
    return D[t]

def airports( G, A, s, t ):
    n = len(G)
    new = [[] for _ in range(n+1)]

    for i in range(n):
        for v, cost in G[i]:
            new[i].append((v, cost))
            new[v].append((i, cost))

    for i in range(n):
        cost = A[i]
        new[n].append((i, cost))
        new[i].append((n, cost))

    return Dijkstra(new,s,t)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( airports, all_tests = True )