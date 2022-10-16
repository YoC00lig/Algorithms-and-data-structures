# W pewnym państwie znajdują się miasta, połączone siecią jednokierunkowych rurociągów, każdy
# o określonej przepustowości. Złoża ropy zostały wyczerpane, jednak w jednym z miast odkryto
# niewy- czerpane źródło nowego rodzaju paliwa. Postanowiono zbudować dwie fabryki w różnych
# miastach oczyszczające nowe paliwo. Z pewnych względów fabryki te nie mogą znajdować się
# w mieście, w którym odkryto nowe złoża i nowe paliwo będzie transportowane istniejącą siecią
# rurociągów. Należy wskazać dwa miasta w których należy zbudować fabryki aby zmaksymalizować
# produkcję oczyszczonego paliwa.
# Proszę zaimplementować funkcję maxflow(G,s), która dla istniejącej sieci rurociągów G i miasta,
# w którym odkryto złoże s, zwróci maksymalną łączną przepustowość do dwóch miast w których należy
# zbudować fabryki. Miasta są ponumerowane kolejnymi liczbami 0,1,2,... Sieć rurociągów opisuje lista
# trójek: (miasto w którym rozpoczyna się rurociąg, miasto w którym się kończy rurociąg, przepustowość rurociągu)
# Przykład Dla sieci G = [(0,1,7),(0,3,3),(1,3,4),(1,4,6),(2,0,9),(2,3,7),(2,5,9),
# (3,4,9),(3,6,2),(5,3,3),(5,6,4),(6,4,8)] oraz miasta s=2 wynikiem jest 25 (miasta 4 i 5).

# Joanna Kulig
# W zadaniu korzystam z algorytmu wyszukującego maksymalny przepływ korzystając z metody Forda-Fulkersona.
# Na początku tworzę nowy graf w postaci macierzowej dokładając dodatkowo jeden nowy wierzchołek (będzie on pełnił rolę ujścia).
# W głównej części algorytmu każde dwa wierzchołki łączę krawędziami z tym nowo dodanym wierzchołkiem i dla tak powstałego grafu
# obliczam maksymalny przepływ od wierzchołka s do tego nowo utworzonego wierzchołka. Jeśli zwiększa to przepływ to aktualizuje maksimum.
# Dodane krawędzie do nowego wierzchołka za każdym razem usuwam.

from zad9testy import runtests
from collections import deque

def FordFulkerson(g, start, end):
    if start == end: return 0
    n = len(g)
    G = [row[:] for row in g]
    P = [-1] * n
    MaxFlow = 0

    def BFS(start, end): # BFS do wyszukiwania ścieżek powiększających
        visited = [False] * n
        visited[start] = True
        q = deque([])
        q.append(start)

        while q:
            u = q.popleft()
            if u == end: return True
            for i in range(n):
                if G[u][i] > 0 and not visited[i]:
                    P[i] = u
                    if i == end: return True
                    visited[i] = True
                    q.append(i)

        return False

    while BFS(start, end):

        path, s, vertex = float("inf"), end, end

        while s != start: # szukam przepływu (przepustowości, najmniejszej krawędzi) na znalezionej ścieżce
            path = min(path, G[P[s]][s])
            s = P[s]

        MaxFlow += path

        while vertex != start: # "odwracanie" krawędzi
            u = P[vertex]
            G[vertex][u] += path
            G[u][vertex] -= path
            vertex = P[vertex]

    return MaxFlow

def maxflow(G, s):
    # graf jest dany w postaci listy krawędzi, szukam liczby wierzchołków, aby móc utworzyć graf w postaci macierzy
    maxi = 0
    for i, j, k in G: maxi = max(max(maxi, i), j )
    n = maxi + 1
    # tworzenie grafu w postaci macierzy
    g = [[0]*(n+1) for _ in range(n+1)]
    for i, j, k in G: g[i][j] = k

    result = 0
    for i in range(n):
        for j in range(i+1, n):
            if i != s and j != s: # znalezione wierzchołki nie mogą być wierzchołkiem s (treść zadania)

                g[i][n] = g[j][n] = float("inf") # tworzę krawędź z dwóch wybranych wierzchołków do dodanego przeze mnie wierzchołka
                x = FordFulkerson(g, s, n)
                result = max(result, x)
                g[i][n] = g[j][n] = 0 # usuwam stworzone przeze mnie krawędzie
    return result

runtests(maxflow, all_tests=True)