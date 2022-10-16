# Zadanie 3. (wymiana walut) Dana jest tabela kursów walut.
# Dla każdych dwóch walut x oraz y wpis K[x][y] oznacza ile trzeba
# zapłacić waluty x żeby otrzymać jednostkę waluty y.
# Proszę zaproponować algorytm, który sprawdza czy istnieje taka waluta z,
# że za jednostkę z można uzyskać więcej niż jednostkę z przez serię wymian walut.


from math import inf, log2

def BF(G, start):
    n = len(G)
    D = [inf] * n
    D[start] = 0

    for i in range(n-1):
        for u in range(n):
            for v in range(n):
                if G[u][v] != 0:
                    if D[v] > D[u] + G[u][v]:
                        D[v] = D[u] + G[u][v]

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0 and D[v] > D[u] + G[u][v]:
                return True
    return False


def Exchange(G, startVal):
    n = len(G)

    for u in range(n):
        for v in range(n):
            if G[u][v] != 0:
                G[u][v] = log2(G[u][v])

    return BF(G, startVal)

