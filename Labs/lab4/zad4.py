# Pewien eksperyment fizyczny generuje bardzo szybko stosunkowo
# krótkie ciągi liczb całkowitych z przedziału od 0 do 10^9 −1.
# Pomiar w eksperymencie polega na okresleniu ile różnych liczb znajduje
# się w danym ciągu. Niestety liczby są generowane tak szybko, że konieczne
# jest zagwarantowanie czasu działania rzędu O(1) na każdy element ciągu
# (pamięć jest dużo mniej krytycznym zasobem). Ciągi są generowane błyskawicznie,
# jeden po drugim. Proszę zaproponować strukturę danych pozwalającą na przeprowadzenie eksperymentu.

# ROZWIĄZANIE
# Skoro pamięć jest dużo mniej krytycznym zasobem, to możemy stworzyć pomocniczą tablicę,
# która będzie przechowywała zliczenia wystąpień każdej liczby z podanego przedziału (tablica długości 10^9).
# Dodatkowo stworzymy zmienną era, tzw. licznik epok, który będzie nas informował o tym, która liczba się
# powtórzyła (jeśli licznik w tablicy będzie większy niż licznik epok, to znaczy, że liczba w którymś momencie się powtórzyła).
# Licznik epok ustawiamy początkowo na 1.

# FUNKCJA INSERTVALUE - Jeśli licznik w tablicy counter dla podanej wartości jest mniejszy niż licznik epok,
# to znaczy że dodajemy wartość która się nie powtórzyła dla podanego ciągu. Przypisujemy mu wtedy wartość
# licznika epok i licznik wartości unikalnych.

# FUNKCJA UNIQUEVALUES - Zwraca liczbę naliczonych wartości unikalnych w podanym ciągu.

# FUNKCJA RESET - wykonywana po każdym ciągu, zwiększamy licznik epok o 1 i zerujemy licznik wartosci unikalnych

class Experiment():
    def __init__(self):
        self.counter = [0] * (10**9)
        self.era = 1
        self.unique = 0

    def InsertValue(self, value):
        if self.counter[value] < self.era:
            self.counter[value] = self.era
            self.unique += 1

    def UniqueValues(self):
        return self.unique

    def Reset(self):
        self.unique = 0
        self.era += 1