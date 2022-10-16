# Zadanie 1. (pokrycie przedziałami jednostkowymi) Dany jest zbiór punktów X = {x1,...,xn} na prostej.
# Proszę podać algorytm, który znajduje minimalną liczbę przedziałów jednostkowych domkniętych,
# potrzebnych do pokrycia wszystkich punktów z X. (Przykład: Jeśli X = {0.25, 0.5, 1.6} to potrzeba
# dwóch przedziałów, np. [0.2,1.2] oraz [1.4,2.4]).

# ROZW: Sortuje punkty niemalejąco, następnie nowy przedział zaczynam od pierwszego niepokrytego.

def CoverIntervals(points):
    n = len(points)
    points.sort()
    cnt = 0
    curr = points[0] + 1 # aktualny koniec
    for i in range(n):
        if points[i] > curr: # nowy początek
            cnt += 1
            curr = points[i] + 1 # nowy koniec

    return curr


test = [0.25, 0.5, 1.6]
print(CoverIntervals(test))