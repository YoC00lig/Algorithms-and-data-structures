# Zadanie 1. (wiele źródeł i ujść) Mamy dany graf skierowany G = (V, E) oraz funkcję c∶ E → N opisującą
# przepustowość każdej krawędzi (liczbę jednostek towaru na godzinę, które mogą się przemieszczać krawędzią).
# Poza tym mamy dany zbiór wierzchołków-fabryk S = {s1,...,sn} oraz zbiór wierzchołków-sklepów T = {t1, . . . , tm}.
# Dla każdej fabryki si znamy liczbę pi określającą ile jednostek towaru na godzinę fabryka może maksymalnie produkować.
# Jednocześnie dla każdego sklepu tj mamy liczbę qj, która mówi ile jednostek towaru na godzinę musi
# do tego sklepu docierać. Proszę podać algorytm, który sprawdza, czy da się zapewnić, żeby do każdego sklepu
# docierało z fabryk dokładnie tyle jednostek towaru ile sklep wymaga jednocześnie nie zmuszając żadnej fabryki
# do przekroczenia swoich możliwości produkcyjnych i nie przekraczając przepustowości żadnej z krawędzi.

# Komentarz. Wystarczy zbudować superźródło z odpowiednimi przepustowościami do fabryk
# i superujście od sklepów, a potem użyć standardowego algorymu.

def BFS(G, start, end, P):
    n = len(G)
    visited = [False]*n
    q = []
    q.append(start)
    visited[start] = True

    while q:
        u = q.pop(0)
        if u == end: return True
        for i in range(n):
            if not visited[i] and G[u][i] > 0:
                q.append(i)
                visited[i] = True
                P[i] = u

    return False

def FordFulkerson(G, start, end):
    n = len(G)
    P = [-1]*n
    MaxFlow = 0

    while BFS(G, start, end, P):
        path, s, vertex = float("inf"), end, end

        while s != start:
            path = min(path, G[P[s]][s])
            s = P[s]

        MaxFlow += path

        while vertex != start:
            u = P[vertex]
            G[u][vertex] -= path
            G[vertex][u] += path
            vertex = P[vertex]

    return MaxFlow


def FactoriesAndShops(factories, shops, graph):
    n = len(graph)
    G = [[0]*(n+2) for _ in range(n+2)]

    for i in range(n):
        for j in range(n): G[i][j] = graph[i][j]

    superfact, supershop = n - 2, n - 1
    for factory in factories: G[superfact][factory[0]] = factory[1]
    for shop in shops: G[shop[0]][supershop] = shop[1]

    maxFlow, summary = FordFulkerson(G, superfact, supershop), 0
    for shop in shops: summary += shop[1]

    return True if maxFlow == summary else False

