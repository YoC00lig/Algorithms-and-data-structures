"""
Zadanie 4. (min/max) Proszę zaimplementować funkcję, która mając na wejściu tablicę n elementów
oblicza jednocześnie jej największy i najmniejszy element wykonując 1.5n porównań.

"""

def MinIMax(T):
    mini = maxi = T[-1]

    for i in range(0, len(T)-1, 2):
        if T[i] > T[i+1]:
            if T[i] > maxi: maxi = T[i]
            if T[i+1] < mini: mini = T[i+1]
        else:
            if T[i+1] > maxi: maxi = T[i+1]
            if T[i] < mini: mini = T[i]

    return mini, maxi
