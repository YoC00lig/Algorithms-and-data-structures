# W roku 2050 spokojny Maksymilian odbywa podróż przez pustynię z miasta A do miasta B. Dro-
# ga pomiędzy miastami jest linią prostą na której w pewnych miejscach znajdują się plamy ropy.
# Maksymilian porusza się 24 kołową cysterną, która spala 1 litr ropy na 1 kilometr trasy.
# Cysterna wyposażona jest w pompę pozwalającą zbierać ropę z plam. Aby dojechać z miasta A
# do miasta B Maksymilian będzie musiał zebrać ropę z niektórych plam (by nie zabrakło paliwa), co każdo-
# razowo wymaga zatrzymania cysterny. Niestety, droga jest niebezpieczna. Maksymilian musi więc tak zaplanować
# trasę, by zatrzymać się jak najmniej razy. Na szczęście cysterna Maksymiliana jest ogromna - po zatrzymaniu
# zawsze może zebrać całą ropę z plamy (w cysternie zmieściłaby się cała ropa na trasie).
# Zaproponuj i zaimplementuj algorytm wskazujący, w których miejscach trasy Maksymilian powi-
# nien się zatrzymać i zebrać ropę. Algorytm powinien być możliwe jak najszybszy i zużywać jak najmniej pamięci.
# Uzasadnij jego poprawność i oszacuj złożoność obliczeniową.
# Dane wejściowe reprezentowane są jako tablica liczb naturalnych T, w której wartość T[i] to ob-
# jętość ropy na polu numer i (objętość 0 oznacza brak ropy). Pola mają numery od 0 do n − 1 a odległość
# między kolejnymi polami to 1 kilometr. Miasto A znajduje się na polu 0 a miasto B na polu n − 1.
# Zakładamy, że początkowo cysterna jest pusta, ale pole 0 jest częścią plamy ropy, którą można zebrać przed
# wyruszeniem w drogę. Zakładamy również, że zadanie posiada rozwiązanie, t.j. da się dojechać z miasta A do miasta B.
# Algorytm należy zaimplementować w funkcji:
# def plan(T):
# ...
# która przyjmuje tablicę z opisem pół T[0], ..., T[n-1] i zwraca listę pól,
# na których należy się zatrzymać w celu zebrania ropy. Lista powinna być posortowana w
# kolejności postojów. Postój na polu 0 również jest częścią rozwiązania.
# Przykład. Dla wejścia:
#      0 1 2 3 4 5 6 7
# T = [3,0,2,1,0,2,5,0] wynikiem jest np. lista [0,2,5].




# Joanna Kulig
# Złożoność czasowa O(nlogn)

# Algorytm zachłannie wybiera najlepsze w zasięgu rozwiązanie.

# Na początku algorytmu tworzę kolejkę priorytetową i wkładam do niej element postaci (-ropa na indeksie 0, indeks 0)
# (minus ze względu na to, że tworzę kolejkę max).
# Następnie algorytm wybiera pozycję zawierającą największą ilość ropy na trasie. (trasa: od najdalszej pozycji, do której
# mogliśmy dotrzeć poprzednio, aż do najdalszej pozycji, na jaką pozwala nam ilość aktualnie zebranej ropy w cysternie)

# Gdyby algorytm nie wybierał największej plamy ropy na trasie, to skróciłoby to zasięg - mogłoby to zwiększyć liczbę tankowań.
# Wybierając zachłannie najlepsze w zasięgu rozwiązanie możemy dotrzeć na miejsce przy najmniejszej liczbie tankowań.


from zad5testy import runtests
from queue import PriorityQueue

def plan(T):
    pq = PriorityQueue()
    prev = reach = 0
    result = []
    pq.put((-T[0], 0)) # zerowy indeks z plamą ropy do kolejki - z tresci zadania wiemy,
    # że istnieje rozwiązanie i da się dojechać z miasta A do B oraz 0 jest częścią plamy ropy
    while pq.qsize() and prev < len(T) - 1: # sprawdzamy dopóki mamy elementy w kolejce i nie dotarliśmy do końca tablicy
        fuel, stop = pq.get() #znaleziono miejsce do zebrania ropy
        fuel = abs(fuel)
        reach += fuel
        result.append(stop)
        if reach >= len(T) - 1: break # jeśli okazuje się, że dotrzemy do końca tablicy to przerywamy pętlę
        for i in range(prev+1, reach+1): # w przeciwnym razie dodaje kolejne indeksy na których jest ropa do kolejki
            if T[i] > 0: pq.put((-T[i], i))
        prev = reach
    return sorted(result)

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( plan, all_tests = True)
