# Zadanie offline 6.
# Szablon rozwiązania: zad6.py
# Dany jest graf nieskierowany G = (V,E) oraz dwa wierzchołki s,t ∈ V.
# Proszę zaproponować i zaimplementować algorytm, który sprawdza, czy istnieje taka krawędź {p, q} ∈ E,
# której usunięcie z E spowoduje wydłużenie najkrótszej ścieżki między s a t (usuwamy tylko jedną krawędź). Algo-
# rytm powinien być jak najszybszy i używać jak najmniej pamięci. Proszę skrótowo uzasadnić jego
# poprawność i oszacować złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję:
# def longer(G, s, t):
#    ...
# która przyjmuje graf G oraz numery wierzchołków s, t i zwraca dowolną krawędź spełniającą warunki
# zadania, lub None jeśli takiej krawędzi w G nie ma. Graf przekazywany jest jako lista list sąsiadów, t.j. G[i]
# to lista sąsiadów wierzchołka o numerze i. Wierzchołki numerowane są od 0. Funkcja powinna zwrócić krotkę
# zawierającą numery dwóch wierzchołków pomiędzy którymi jest krawędź spełniająca warunki zadania, lub None jeśli
# takiej krawędzi nie ma. Jeśli w grafie oryginalnie nie było ścieżki z s do t to funkcja powinna zwrócić None.
# Przykład. Dla argumentów:
#     G = [ [1, 2],
#           [0, 2],
# [0, 1] ] s=0
# t=2
# wynikiem jest np. krotka: (0, 2)

# Joanna Kulig
# ad1. Na początku zapisuję przechodząc BFS-em przez graf odległości wszystkich wierzchołków
# od wierzchołka S w tabeli dist.

# ad2. Jeśli odległość od s do t jest -1, to znaczy, że nie ma żadnej ścieżki od s do t, czyli usunięcie
# jakiejkolwiek krawędzi niczego nie zmieni.

# ad3. Potem przechodzę algorytmem podobnym do BFS od tyłu (od punktu t) w górę, czyli tam,
# gdzie odległość jest mniejsza niż aktualnie. Przy tym przechodzeniu zliczam, ile jest takich krawędzi,
# które prowadzą o 1 niżej w grafie (są wcześniej).
# ad4. Jeśli jest tylko jedna taka na danym poziomie, to znaczy, że to ją należy usunąć.
# Jeśli cały graf został odwiedzony i nie znaleziono takiej krawędzi to zwracam None

# Złożoność obliczeniowa O (V+E) - dodatkowy for w drugim BFS nie psuje złożoności, ponieważ on tylko
# kontroluje poziom na którym się znajdujemy.

from zad6testy import runtests
import collections

def longer(G, s, t):
    dist = [-1] * len(G)
    Q = collections.deque([])
    dist[s] = 0
    Q.append(s)

    # ad1 O (V+E)
    while Q:
        u = Q.popleft()
        for v in G[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                Q.append(v)
    # ad2
    if dist[t] == -1: return None

    # ad3 O(V+E)
    visited = [0] * len(G)
    visited[t] = 1
    Q.append(t)
    cnt = 1
    A = B = -1
    while Q:
        odw1 = odw2 = 0
        for _ in range(cnt):
            u = Q.popleft()
            for v in G[u]:
                if dist[v] < dist[u]:
                    odw2 += 1
                    if visited[v] == 0:
                        visited[v] = 1
                        A, B = u, v
                        odw1 += 1
                        Q.append(v)

        if odw2 == 1: # ad4
            if A > B: return (B, A)
            else: return (A, B)

        cnt = odw1

    return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )