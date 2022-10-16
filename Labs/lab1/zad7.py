"""
Zadanie 7. (szukanie sumy) Dana jest posortowana tablica A[1...n] oraz liczba x.
Proszę napisać program, który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x.
"""


def FindSum(T, x):
    i, j = 0, len(T) - 1

    while i != j:
        if T[i] + T[j] == x: return i, j
        elif T[i] + T[j] > x: j -= 1
        else: i += 1

    return False

T= [1,3,5,6,7,10]
print(FindSum(T, 9))