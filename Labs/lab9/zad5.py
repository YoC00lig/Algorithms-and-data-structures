# Zadanie 3. (najkrósze ścieżki w DAGu) Jak znaleźć najkrótsze ścieżki z wierzchołka s do
# wszystkich innych w acyklicznym grafie skierowanym?

# Najpierw sortuje topologicznie DAG, następnie przechodzę przez tablicę tych posortowanych wierzchołkow
# i wykonuje relaksację dla wszystkich sąsiadów tych wierzchołków.

# O(V+E)

def TopoSort(G):
     n = len(G)
     visited = [False] * n
     result = [-1] * n
     idx = n-1

     def DFS(u):
         nonlocal visited, result, idx
         visited[u] = True
         for v, _ in G[u]:
             if not visited[v]:
                 DFS(v)
         result[idx] = u
         idx -= 1

     for i in range(n):
         if not visited[i]:
             DFS(i)

     return result


def shortestPaths(G):
    n = len(G)
    t = TopoSort(G)
    D = [float("inf")] * n
    D[t[0]] = 0

    for w in t:
        for v, weight in G[w]:
            if D[w] + weight < D[v]:
                D[v] = D[w] + weight

    return D

