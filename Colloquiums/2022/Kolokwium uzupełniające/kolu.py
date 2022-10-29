# Odwracam krawędzie grafu, zliczam dla każdego wierzchołka ilośc wchodzących do niego krawędzi
# jeśli do jakiegoś wierzchołka nie ma wchodzących krawędzi, to znaczy, że wierzchołek może zostać wykorzystany
# ( nie ma żadnego innego wierzchołka, który musi go poprzedzać ).
# Następnie przechodzę bfsem po tak powstałym grafie, za każdym razem przetwarzając dany wierzchołek 
# "usuwam" krawędzie prowadzące z niego do innych wierzchołków.

from collections import deque

def Reverse(G): 
    n = len(G)
    indeg = [0]*n
    new = [[] for _ in range(n)]
    for i in range(n):
        for v in G[i]:
            new[v].append(i)
            indeg[i] += 1
    return new, indeg

def swaps( disk, depends ):
    n = len(depends)
    G, deg = Reverse(depends)
    q = deque([])
    visited = [False] * n
    parents = [None] * n
    change_num = [float("inf")] * n

    for i in range(n):
        if deg[i] == 0:
            q.append(i)
            change_num[i] = 0
            visited[i] = True

    while q:
        u = q.popleft()

        for v in G[u]:
            deg[v] -= 1

            if deg[v] == 0 and not visited[v]:

                visited[v], parents[v] = True, u
                change_num[v] = change_num[u] + int(disk[u] != disk[v])
                if disk[v] == disk[u]: q.appendleft(v)
                # lepiej wcześniej przetworzyć ten wierzchołek, który nie wymaga zmiany dysku
                else: q.append(v)

    return max(change_num)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( swaps, all_tests = True )