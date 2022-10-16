# Dana jest posortowana tablica A[1...n] oraz liczba x. Proszę napisać program,
# który stwierdza czy istnieją indeksy i oraz j takie, że A[i] + A[j] = x

# ROZWIĄZANIE
# Przy użyciu dwóch wskażników - początkowo wskazujących na początek i koniec listy - obliczam sumę liczb na które wskazują.
# jeśli suma jest za duża, to mogę ją zmniejszyć poruszając się prawym wskaźnikiem o jeden w lewo, jeśli jest za mała,
# to mogę ją zwiększyć poruszając się w prawo lewym wskaźnikiem.

def FindSum(T,x):
    left = 0
    right = len(T) - 1
    while left < right:
        suma = T[left] + T[right]
        if suma == x: return left,right
        elif suma > x: right -= 1
        elif suma < x: left += 1
    return False # nie ma takiej sumy