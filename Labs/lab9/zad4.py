# Zadanie 2. (dobry początek) Wierzchołek v w grafie skierowanym nazywamy dobrym początkiem jeśli
# każdy inny wierzchołek można osiągnąć scieżką skierowaną wychodzącą z v. Proszę podać algorytm,
# który stwierdza czy dany graf zawiera dobry początek.

# jeśli jest taki wierzchołek, to jest nim ten wierzchołek, w którym ostatni raz wywołujemy DFS

def GoodStart(G):
    n = len(G)
    visited = [False] * n

    def DFS(v, visited):
        visited[v] = True
        for i in G[v]:
            if not visited[i]:
                DFS(i, visited)

    vert = 0
    for i in range(n):
        if not visited[i]:
            DFS(i, visited)
            vert = i

    visited = [False] * n
    DFS(vert, visited)
    for i in visited:
        if not i: return False
    return vert

G = [[1,3],[4],[0],[2],[]]
print(GoodStart(G))

