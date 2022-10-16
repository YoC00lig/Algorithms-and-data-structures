# Zadanie 4. (logarytmy) Mamy dany graf G = (V, E) z wagami w∶ E → N−{0} (dodatnie liczby naturalne).
# Chcemy znalezc scieżkę z wierzchołka u do v tak, by iloczyn wag był minimalny. Omówic rozwiązanie
# (bez implementacji)

# log(a*b) = loga + logb  <-- zamieniamy wagi krawędzi na logarytmy i potem zwykła dijkstra

from math import log, inf, e
from queue import PriorityQueue

def CreateGraph(G):
    n = len(G)
    g = [[] for _ in range(n)]

    for u in range(n):
        for v, weight in G[u]:
            g[u].append((v, log(weight)))
    return g

def Dijkstra(G,start,end):
    n = len(G)
    D = [inf]*n
    P = [None]*n
    q = PriorityQueue()
    q.put((0,start,None))

    while not q.empty():
        weight, u, parent = q.get()
        if weight < D[u]:
            D[u] = weight
            P[u] = parent
            if u == end: break
            for v,w in G[u]:
                if D[v] == inf:
                    q.put((D[u] + w, v, u))
    return P, D

def GetPath(P, v):
    path = []
    while v is not None:
        path.append(v)
        v = P[v]
    path.reverse()
    return path

def Logarithms(G, start, end):
    g = CreateGraph(G)
    p,d = Dijkstra(g,start,end)
    if d[end] == inf: return -1
    product = int(e**d[end] + 0.5)
    return GetPath(p, end), product

