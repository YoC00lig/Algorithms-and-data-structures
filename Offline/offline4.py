# Inwestor planuje wybudować nowe osiedle akademików. Architekci przedstawili projekty budynków,
# z których inwestor musi wybrać podzbiór spełniający jego oczekiwania. Każdy budynek
# reprezentowany jest jako prostokąt o pewnej wysokości h, podstawie od punktu a do punktu b,
# oraz cenie budowy w (gdzie h, a, b i w to liczby naturalne, przy czym a < b). W takim budynku
# może mieszkać h ⋅ (b − a) studentów.

# Proszę zaimplementować funkcję:
# def select_buildings(T, p):
# ...

# która przyjmuje:
# • Tablicę T zawierająca opisy n budynków. Każdy opis to krotka postaci (h, a, b, w), zgodnie
# z oznaczeniami wprowadzonymi powyżej.
# • Liczbę naturalną p określającą limit łącznej ceny wybudowania budynków.

# Funkcja powinna zwrócić tablicę z numerami budynków (zgodnie z kolejnością w T, numerowanych
# od 0), które nie zachodzą na siebie, kosztują łącznie mniej niż p i mieszczą maksymalną liczbę
# studentów. Jeśli więcej niż jeden zbiór budynków spełnia warunki zadania, funkcja powinna zwrócić
# zbiór o najmniejszym łącznym koszcie budowy. Dwa budynki nie zachodzą na siebie, jeśli nie mają
# punktu wspólnego.
# Można założyć, że zawsze istnieje rozwiązanie zawierające co najmniej jeden budynek. Funkcja
# powinna być możliwie jak najszybsza i zużywać jak najmniej pomięci. Należy bardzo skrótowo
# uzasadnić jej poprawność i oszacować złożoność obliczeniową.

# Przykład. Dla argumentów:
# T = [ (2, 1, 5, 3),
# (3, 7, 9, 2),
# (2, 8, 11, 1) ]
# p = 5
# Wynikiem jest tablica: [ 0, 2 ].


# ROZWIĄZANIE
# Budynki sortujemy po współrzędnej b.
# f(i,p) - maksymalna liczba studentów, którzy mają mieszkać w budynkach od 0 do i,
# które na siebie nie nachodzą i kosztują najwyżej p
# f(i,p) = max(f(i-1,p), student(i) + f(prev(i), p - cost(i))
#               ^                           ^
#               |                           |
#               |                           |
#       Nie budujemy i-tego        Budujemy i-ty budynek
#            budynku

# Trzeba zdefiniować trzy pomocnicze funkcje:
# def students(i) - ile studentów mieści się w budynku i-tym
# def prev(i) - pierwszy budynek przed i-tym nie nachodzący na niego
# def cost(i) - koszt wybudowania i-tego budynku

def binary_search(T, left, right, i): # do wyszukiwania jak najdalszego budynku nie zachodzącego na obecny
    # binary search redukuje złożonosć wyszukiwania preva z O(n^2) do O(nlogn)
    if left > right: return right
    mid = (left + right) // 2
    if T[mid][2] < T[i][1]: return binary_search(T, mid + 1, right, i)
    else: return binary_search(T, left, mid - 1, i)

def prev(T):  # do mapowania poprzednich nienachodzących budynków dla każdego budynku O(nlogn)
    prevs = [None for _ in range(len(T))]
    for i in range(len(T)): prevs[i] = binary_search(T, 0, len(T)-1, i)
    return prevs

def cost(T): # do mapowania kosztów O(n)
    costs = [-1 for _ in range(len(T))]
    for i in range(len(T)): costs[i] = T[i][3]
    return costs

def student(T):  # do mapowania liczby studentów O(n)
    n = len(T)
    st = [-1 for _ in range(n)]
    for i in range(n): st[i] = T[i][0] * (T[i][2] - T[i][1])
    return st

def GetSolution(T, building, money, dp, prevs, students, costs): # tworzenie rozwiązania
    # warunek końca rekurencji - skończyły się budynki lub pieniądze
    if money <= 0 or building < 0: return []
    # 1. mamy pieniądze do wykorzystania na ten budynek
    if money >= costs[building]:
        if building == 0:
            return [T[building][4]]
        elif dp[building][money] == dp[prevs[building]][money - costs[building]] + students[building]:
            return [T[building][4]] + GetSolution(T, prevs[building], money - costs[building], dp, prevs, students, costs)
        elif dp[building][money] == students[building]:
            return [T[building][4]]
    # 2. nie mamy pieniędzy do wykorzystania na ten budynek
    if building == 0: return []
    else: return GetSolution(T, building-1, money, dp, prevs, students, costs)

def select_buildings(T , p): #O(np + nlogn)
    n = len(T)
    for i in range(n): # dodaje na koniec indeks w oryginalnej tablicy, aby móc potem odzyskać go tworząc rozwiązanie
        T[i] = [T[i][0], T[i][1], T[i][2], T[i][3], i]
    T.sort(key=lambda x: x[2])

    # Tablice pomocnicze, żeby się nie pogubić w indeksach w tablicy T
    students = student(T)
    prevs = prev(T)
    costs = cost(T)
    dp = [[0 for _ in range(p + 1)] for _ in range(n)]

    # BASECASE - uzupełniamy tabelę dla budynku numer 0
    for i in range(costs[0], p + 1):
        dp[0][i] = students[0]

    for building in range(1, n):
        for money in range(p + 1):
            if prevs[building] is not None and costs[building] <= money:
                dp[building][money] = max(dp[building - 1][money], dp[prevs[building]][money - costs[building]] + students[building])
            elif costs[building] <= money:
                dp[building][money] = max(dp[building - 1][money], students[building])
            else:
                dp[building][money] = dp[building - 1][money]

    # minimalizowanie kosztów
    MaxStudentsNum = dp[-1][-1]
    MinCost = p # minimalna cena to co najwyżej cena p
    for c in range(p, -1, -1): # cofamy się w ostatnim wierszu, aby znaleźć, jaka jest najmniejsza cena przy której można pomieścić maxStudentsNum studentów
        if dp[n - 1][c] < MaxStudentsNum: break # jeśli jest to już mniejsza liczba studentów niż maksymalna, to przerywamy pętlę
        elif dp[n - 1][c] == MaxStudentsNum: MinCost = c # jeśli istnieje mniejsza cena dla tej samej liczby studentów to aktualizujemy minimalną cenę

    return sorted(GetSolution(T, n-1, MinCost, dp, prevs, students, costs))

