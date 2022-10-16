# Zadanie 3. (BFS i najkrótsze ścieżki) Proszę zaimplementować algorytm BFS tak, żeby znajdował
# najkrótsze ścieżki w grafie i następnie, żeby dało się wypisać najkrotszą ścieżkę z zadanego
# punktu startowego do wskazanego wierzchołka.

from collections import deque

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

def bfs(graph, start, end): # reprezentacja grafu - lista sąsiedztwa
    # zapisujemy wierzchołki w tablicy parents, żeby móc odtworzyć sciezke
    if start == end: return []
    n = len(graph)
    parents = [-1] * n
    queue = deque([])
    queue.append(start)

    while queue:
        u = queue.popleft()
        if u == end: break
        for v in graph[u]:
            if parents[v] < 0:
                parents[v] = u
                queue.append(v)

    return GetPath(parents, start, end)