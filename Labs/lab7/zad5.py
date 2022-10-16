# Zadanie 6. (suma odległości) Dana jest posortowana tablica A zawierająca n liczb i celem jest wyzna-
# czenie liczby x takiej, że wartość ∑n−1 i=0 ∣A[i] − x∣ jest minimalna. Proszę zaproponować algorytm, uzasadnić
# jego poprawność oraz ocenić złożoność obliczeniową.

# jeśli nieparzysta liczba elmentów to bierzemy element ze środka
# jęsli parzysta to mamy dwie mediany i bierzemy dowolny pubkt z przedziału <m1,m2>

def lol(T):
    n = len(T)
    return T[n//2 + 1]