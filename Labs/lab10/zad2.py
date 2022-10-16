# Zadanie 2. (domknięcie przechodnie) Proszę zaimplementować algorytm obliczający domknięcie prze-
# chodnie grafu reprezentowanego w postaci macierzowej (domknięcie przechodnie grafu G, to graf
# nad tym samym zbiorem wierzchołków, który dla każdych dwóch wierzchołków u i v ma krawędź
# z u do v wtedy i tylko wtedy, gdy w G istnieje ścieżka z u do v.

# macierze

# Floyd Warshall

def TransitiveClosure1(G): # O(n^3)
    n = len(G)
    dp = [[False] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if G[i][j]: dp[i][j] = True

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dp[i][j] = dp[i][k] and dp[k][j]

    return dp




