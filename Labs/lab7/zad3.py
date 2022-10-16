# Zadanie 3. (ładowanie przyczepy) Mamy przyczepę o pojemności K kilogramów oraz zbiór
# ładunków o wagach w1, . . . , wn. Waga każdego z ładunków jest potęgą dwójki
# (czyli, na przykład, dla siedmiu ładunków wagi mogą wynosić 2, 2, 4, 8, 1, 8, 16,
# a pojemność przyczepy K = 27). Proszę podać algorytm zachłanny (i uzasadnić jego poprawność),
# który wybiera ładunki tak, że przyczepa jest możliwie maksymalnie zapełniona (ale bez przekraczania
# pojemności) i jednocześnie użyliśmy możliwie jak najmniej ładunków. (Ale jeśli da się np. załadować
# przyczepę do pełna uzywając 100 ładunków, albo zaladować do pojemności K − 1 używając jednego ładunku,
# to lepsze jest to pierwsze rozwiązanie).

# GREEDY APPROACH: Bierz najcięższy możliwy

# Dowód poprawności
# załóżmy, że istnieje rozwiązanie optymalne, które przynajmniej raz nie bierze największego możliwego elemtnu.

# Przypadek 1) z mniejszych wag nie jesteśmy w stanie zbudować wagi cięższej (nie ma tylu powtórzeń danych mniejszych wag).
# wtedy algorytm zapełni ciężarówkę w mniejszym stopniu. Stąd sprzeczność - według polecenia jeśli da się zapełnić
# bardziej, to jest to lepsze rozwiązanie

# Przypadek 2) z mniejszych wag można zbudować wagę cięższą - w pewnym momencie algorytmu dochodzimy do momentu,
# kiedy wszystkie mniejsze wagi możemy zastąpić jedną cięższą wagą. Stąd sprzeczność - algorytm nie użyłby
# najmniejszej ilości wag.

def load(weights, K):
    weights.sort()
    cnt = 0
    for i in range(len(weights)-1,-1,-1):
        if weights[i] <= K:
            cnt += 1
            K -= weights[i]
    return cnt