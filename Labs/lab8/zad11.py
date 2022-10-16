# Zadanie 2. (czy nieskierowany?) Proszę podać algorytm, który mając na wejściu graf G
# reprezentowany przez listy sąsiedztwa sprawdza, czy jest nieskierowany (czyli czy dla
# każdej krawędzie u → v istnieje także krawędź przeciwna).

def undirected(G):
    n = len(G)
    C = [[0]*n for _ in range(n)]
    cnt = 0

    for u in range(n):
        for v in G[u]:
            C[u][v] += 1
            # znaleźliśmy nową krawędź i liczba krawędzi od u do v jest większa niz liczba krawedzi z v do u
            if C[u][v] > C[v][u]: cnt += 1
            else: cnt -= 1

    return not cnt
