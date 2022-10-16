# Mamy daną N elementową tablicę T liczb rzeczywistych, w której liczby zostały wygenerowane
# z pewnego rozkładu losowego. Rozkład ten mamy zadany jako k przedziałów [a1,b1],[a2,b2],...,[ak,bk]
# takich, że i-ty przedział jest wybierany z prawdopodobieństwem ci, a liczba z przedziału (x ∈ [ai, bi])
# jest losowana zgodnie z rozkładem jednostajnym. Przedziały mogą na siebie nachodzić. Liczby ai,bi są
# liczbami naturalnymi ze zbioru {1,...,N}. Proszę zaimplementować funkcję SortTab(T, P) sortująca
# podaną tablicę i zwracająca posortowa- ną tablicę jako wynik. Pierwszy argument to tablica do
# posortowania a drugi to opis przedziałów w postaci:
# P = [(a_1,b_1,c_1), (a_2,b_2,c_2), ..., (a_k,b_k,c_k)]}.
# Na przykład dla wejścia:
    # T = [6.1, 1.2, 1.5, 3.5, 4.5, 2.5, 3.9, 7.8]
    # P = [(1, 5, 0.75) , (4, 8, 0.25)]
# po wywołaniu SortTab(T,P) tablica zwrócona w wyniku powinna mieć postaci:
# T = [1.2, 1.5, 2.5, 3.5, 3.9, 4.5, 6.1, 7.8]
# Algorytm powinien być możliwie jak najszybszy.
# Proszę podać złożoność czasową i pamięciową zaproponowanego algorytmu.

# Algorytm polega na tym, aby częściowo zlekceważyć tablicę P i zauważyć, że można podzielić
# przedział [0,n] na zbiór przedziałów jednostkowych w których jest rozkład jednostajny.
# W zadaniu korzystam więc z algorytmu Bucket Sort, gdzie kubełkami są przedziały jednostkowe.
# Drobna modyfikacja polega na tym, że w obrębie kubełków liczby sortuję także bucket
# sortem o n kubełkach (n to liczba elementów znajdujących się w kubełkach po pierwszym bucket sorcie).
# Wyjątkiem jest mała liczba elementów w kubełku, tam lepiej sprawdzi się insertion sort,
# który dla małej ilości danych jest bardzo szybki.

def SortTab(T, P):
    maxi = int(max(T)+1)
    buckets = [[] for _ in range(maxi)]
    idx = 0
    for elem in T:
        buckets[int(elem)].append(elem)

    for bucket in buckets:
        n = len(bucket)

        if len(bucket) <= 50:
            # insertion sort
            for i in range(1, n):
                j = i - 1
                key = bucket[i]
                while j >= 0 and bucket[j] > key:
                    bucket[j + 1] = bucket[j]
                    j -= 1
                bucket[j + 1] = key
        else:
            # Bucket sort v2
            if len(bucket) <= 1: return
            k = max(bucket) - min(bucket)
            buckets = [[] for _ in range(n)]
            interval = k / n
            for elem in bucket:
                buckets[int((elem - min(bucket)) // interval)].append(elem)
            i = 0
            for b in buckets:
                n = len(b)
                for i in range(1, n):
                    j = i - 1
                    key = b[i]
                    while j >= 0 and b[j] > key:
                        b[j + 1] = b[j]
                        j -= 1
                    b[j + 1] = key
                for elem in b:
                    bucket[i] = elem
                    i += 1

        for number in bucket:
            T[idx] = number
            idx += 1
    return T