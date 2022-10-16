# Zadanie 6. (najlepszy korzeń) Dany jest acykliczny, spójny, nieskierowany, ważony
# graf T (czyli T jest tak naprawdę ważonym drzewem). Proszę wskazać algorytm, który
# znajduje taki wierzchołek T, z którego odległość do najdalszego wierzchołka jest minimalna.


# najdalszy wierzchołek jaki znajdziemy z dowolnego wierzchołka będzie jednym z dwóch końców średnicy w drzewie.

from math import inf
def FindDiameter(G):
    n = len(G)
    dist = [inf] * n
    visited = [0] * n
    era = 1

    def DFS(u):
        visited[u] = era
        for v, weight in G[u]:
            if visited[v] != era:
                dist[v] = dist[u] + weight
                DFS(v)

    dist[0] = 0
    DFS(0)
    first_diameter_end_vertex = dist.index(max(dist))  # ostatni wierzchołek pierwszej średnicy

    era += 1
    dist[first_diameter_end_vertex] = 0
    DFS(first_diameter_end_vertex) # szukam odległsci od tego wierzchołka do reszty
    second_diameter_end_vertex = dist.index(max(dist))  # drugi koniec średnicy
    dist1 = dist[:]

    era += 1
    dist[second_diameter_end_vertex] = 0
    DFS(second_diameter_end_vertex)
    dist2 = dist[:]

    return dist1, dist2


def best_root(G):
    n = len(G)
    d1, d2 = FindDiameter(G)
    best, mindist = None, inf

    for u in range(n):
        maxidist = max(d1[u], d2[u])
        if maxidist < mindist:
            mindist = maxidist
            best = u
    return best, mindist

# gorsza złozonosc - sprawdzamy dla kazdego wierzchołka
from collections import deque

def BFS(G, start):
    n = len(G)
    D = [float("inf")] * n
    visited = [False] * n
    Q = deque([])

    visited[start] = True
    D[start] = 0
    Q.append(start)

    while Q:
        v = Q.popleft()
        for u in G[v]:
            if not visited[u]:
                visited[u] = True
                D[u] = D[v] + 1
                Q.append(v)

    return max(D)

def BestRoot(G):
    bestroot = dist = prev = 0

    for i in range(len(G)):
        prev = dist
        dist = min(dist, BFS(G, i))
        if dist != prev: bestroot = i

    return bestroot, dist


