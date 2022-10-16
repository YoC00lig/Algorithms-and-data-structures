# zadanie 6. (wyszukiwanie binarne) Proszę zaimplementować funkcję,
# która otrzymuje na wejściu po- sortowaną niemalejąco tablicę A o
# rozmiarze n oraz liczbę x i sprawdza, czy x występuje w A. Jeśli tak,
# to zwraca najmniejszy indeks, pod którym x występuje.

def binsearch(T, val):
    left, right = 0, len(T) - 1

    while left <= right:
        mid = (left+right)//2
        if T[mid] == val: return mid
        elif T[mid] < val: left = mid + 1
        else: right = mid - 1
    return False