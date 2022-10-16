#  (Głodna żaba) Pewna żaba skacze po osi liczbowej. Ma się dostać z zera do n − 1,
#  skacząc wyłącznie w kierunku większych liczb. Skok z liczby i do liczby j (j > i)
#  kosztuje ją j − i jednostek energii, a jej energia nigdy nie może spaść poniżej
#  zera. Na początku żaba ma 0 jednostek energii, ale na szczęście na niektórych
#  liczbach—także na zerze—leżą przekąski o określonej wartości energetycznej
#  (wartość przekąki dodaje się do aktualnej energii Zbigniewa).
#  Proszę zaproponować algorytm, który oblicza minimalną liczbę skoków potrzebną
#  na dotarcie z 0 do n−1 majać daną tablicę A z wartościami energetycznymi przekąsek na każdej z liczb.

# Greedy approach O(n) - nie wiem czy poprawne
from queue import PriorityQueue

def zbigniew1(A):
    n = len(A)
    q = PriorityQueue()
    q.put((-A[0], 0))
    energy = 0
    last = 0
    cnt = 0
    result = []
    while q.qsize() > 0:
        snack, ind = q.get()
        cnt += 1
        energy -= snack
        result.append(ind)
        if energy >= n - 1:
            break
        for i in range(last + 1, energy + 1):
            if A[i] > 0:
                q.put((-A[i], i))
        last = energy

    if energy < n - 1:
        return -1
    return cnt

# f(i, j) - minimalna liczba skoków, żeby dostać się do i-tego pola i mieć co najmniej j jednostek
# energii już po zjedzeniu przekąski

# dynamic programming approach O(n^2)
from math import inf
def zbigniew2(arr):
    n = len(arr)
    SUM = sum(arr)
    F = [[inf for _ in range(SUM + 1)] for _ in range(n)]

    for i in range(arr[0] + 1):
        F[0][i] = 0

    for TO in range(1, n):
        for ENERGY in range(SUM):
            for FROM in range(TO):
                eng = ENERGY + TO - FROM - arr[TO]
                if eng < TO - FROM or eng > SUM or eng < 0:
                    continue
                F[TO][ENERGY] = min(F[TO][ENERGY], F[FROM][eng] + 1)

    return min(F[n - 1][i] for i in range(SUM + 1))