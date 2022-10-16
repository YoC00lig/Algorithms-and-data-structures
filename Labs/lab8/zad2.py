# Zadanie 2. (cykl na cztery) Dany jest graf nieskierowany G zawierający n wierzchołków.
# Zaproponuj algorytm, który stwierdza czy w G istnieje cykl składający się z dokładnie
# 4 wierzchołków.
# Zakładamy, że graf reprezentowany jest przez macierz sasiedztwa A.


# O(v^2) - zamieniam na listę sąsiedztwa
def CreateAdjList(G):
    n = len(G)
    graph = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if G[i][j]: graph[i].append(j)
    return graph

def Find4Cycle(G):
    n = len(G)
    G2 = CreateAdjList(G)
    C = [[-1 for _ in range(n)] for _ in range(n)]

    for u in range(n):
        for i in range(1,len(G2[u])):
            for j in range(i):
                v = G2[u][i]
                w = G2[u][j]
                if C[v][w] < 0: C[v][w] = u
                else: return v, C[v][w], w, u

    return None

# dla macierzy O(n^3)
def Find4CycleMatrix(G):
    n = len(G)
    for u in range(1,n):
        for v in range(u):
            prev = None
            for w in range(n):
                if G[u][w] and G[v][w]:
                    if prev: return u, w, v, prev
                    prev = w
    return None

# znajdowanie K-wierzchołkowego cyklu
def FindKCycle(G,k):
    n = len(G)
    visited = [False] * n
    cycle = [None] * k
    result = []

    def DFS(i, idx):
        cycle[idx] = i
        if idx == k - 1: # sprawdzamy, czy ostatni wierzchołek i da się połączyć z pierwszym wierzchołkiem cyklu
            if G[i][cycle[0]] == 1: result.append(cycle.copy())
            return

        visited[i] = True
        for j in range(n):
            if G[i][j] == 1 and not visited[j]:
                if idx == 0: G[i][j] = G[j][i] = -1 # krawędź oznaczona jako odwiedzona, żeby zapobiec szukaniu tego samego cyklu tylko w przeciwną stronę
                DFS(j, idx+1)

        visited[i] = False

    # sprawdzanie każdego możliwego cyklu zaczynającego się w i
    for i in range(n-k+1):
        DFS(i, 0)
        visited[i] = True
    # only naprawianie grafu
    for i in range(n):
        for j in range(n):
            G[i][j] = abs(G[i][j])

    return result
