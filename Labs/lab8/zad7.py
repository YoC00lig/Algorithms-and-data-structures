# Zadanie 5. (krawędzie 0/1) Dana jest mapa kraju w postaci grafu G = (V, E).
# Kierowca chce przejechać z miasta (wierzchołka) s to miasta t. Niestety niektóre drogi (krawędzie) są płatne.
# Każda droga ma taką samą jednostkową opłatę. Proszę podać algorytm, który znajduje trasę wymagającą jak
# najmniejszej liczby opłat. W ogólności graf G jest skierowany, ale można najpierw wskazać algorytm dla
# grafu nieskierowanego.

# nieskierowany

from collections import deque
from math import inf

def GetPath(parents, start, end):
    if parents[end] < 0: return []
    path = []
    u = end
    while u != start:
        path.append(u)
        u = parents[u]
    path.append(start)
    path.reverse()
    return path

def bfs(graph, start, end):
    n = len(graph)
    dist = [inf] * n
    queue = deque([])
    parents = [-1] * n
    dist[start] = 0
    queue.append(start)

    while queue:
        u = queue.popleft()
        if u == end: break
        for edge in graph[u]:
            v = edge[0]
            weight = edge[1]
            if dist[v] > dist[u] + weight:
                dist[v] = dist[u] + weight
                parents[v] = u
                if weight == 0: queue.appendleft(v)
                else: queue.append(v)

    return GetPath(parents,start,end)

# skierowany ????