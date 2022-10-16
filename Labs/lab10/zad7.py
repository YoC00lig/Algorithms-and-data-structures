# W pewnym państwie, w którym znajduje się N miast, postanowiono połączyć wszystkie miasta sie-
# cią autostrad, tak aby możliwe było dotarcie autostradą do każdego miasta. Ponieważ kontynent, na
# którym leży państwo jest płaski położenie każdego z miast opisują dwie liczby x, y, a odległość w linii
# prostej pomiędzy miastami liczona w kilometrach wyraża się wzorem len = √(x1 − x2)2 + (y1 − y2)2
# Z uwagi na oszczędności materiałów autostrada łączy dwa miasta w linii prostej.
# Ponieważ zbliżają się wybory prezydenta, wszystkie autostrady zaczęto budować równocześnie i
# jako cel postanowiono zminimalizować czas pomiędzy otwarciem pierwszej i ostatniej autostrady.
# Czas budowy autostrady wyrażony w dniach wynosi ⌈len⌉ (sufit z długości autostrady wyrażonej w km).
# Proszę zaimplementować funkcję highway(A), która dla danych położeń miast wyznacza mini- malną liczbę dni
# dzielącą otwarcie pierwszej i ostatniej autostrady.

# Przykład
# Dla tablicy A =[(10,10),(15,25),(20,20),(30,40)] wynikiem jest 7
# (Autostrady pomiędzy miastami 0-1, 0-2, 1-3).
# Joanna Kulig
# W Algorytmie korzystam z algorytmu Kruskala.
# Na początku tworzę graf pełny w postaci listy krawędzi o krawędziach ważonych
# o wagach wyliczonych z podanego w zadaniu wzoru. Krawędzie sortuje rosnąco według wag.
# Następnie w pętli wyznaczam minimalne drzewo rozpinające stworzonego grafu, sprawdzam
# i aktualizuje minimum ( minimalną liczbę dni będącą wynikiem ) oraz usuwam najmniejszą krawędź.
# Robię to dopóki graf jest spójny. Kiedy graf przestaje być spójny zwracam wynik
from math import ceil

def KRUSKAL(G,V, best):
    parent = [i for i in range(V)]
    rank = [0] * V

    # struktura find-union z wykładu, przerobiona na tablice zamiast klas
    def find(x):
        if parent[x] != x: parent[x] = find(parent[x])
        return parent[x]

    def union(x, y):
        a = find(x)
        b = find(y)
        if a == b: return
        if rank[a] > rank[b]: parent[b] = a
        else:
            parent[a] = b
            if rank[a] == rank[b]: rank[b] += 1

    MST = []
    for a, b, c in G:
        if find(a) != find(b):
            MST.append((a, b, c))
            if abs(c - MST[0][2]) >= best: return MST[0], False # jeśli otrzymaliśmy liczbę dni większą niż dotychczasowy najlepszy wynik lub równą, to nie ma sensu sprawdzać dalej
            elif len(MST) == V - 1: break # jedną z własności drzew jest, że V = E + 1, więc jeśli utworzone MST ma już tyle krawędzi to nie ma potrzeby iterować dalej po krawędziach
            union(a, b)

    return MST, True

def highway( A ):
    G = []
    V = len(A)
    minimum = float("inf")

    # tworzę listę krawedzi
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            G.append((i, j, ceil(((A[i][0]-A[j][0])**2 + (A[i][1]-A[j][1])**2)**0.5)))

    G = sorted(G, key=lambda weight: weight[2])

    while len(G) >= V - 1:

        B, flag = KRUSKAL(G, V, minimum)

        if not flag: # stworzone drzewo miało gorszy wynik niż dotychczasowy, więc usuwam krawędź bez aktualizacji minimum
            G.remove(B)
            continue

        if len(B) < V - 1: break # W drzewach E musi być równe V - 1, jeśli liczba krawędzi jest mniejsza to znaczy że graf nie jest spójny

        minimum = min(minimum, abs(B[0][2] - B[-1][2]))
        G.remove(B[0])

    return minimum