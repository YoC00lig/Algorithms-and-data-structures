# Proszę zaimplementować algorytm znajdowania k-go co do wielkości
# elementu w tablicy n elementowej w “spodziewanym” czasie O(n) na podstawie randomizowanego Partition z QuickSort’a

# ROZWIĄZANIE
# Wykorzystuję algorytm Quick Select

from random import randint


def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def Partition(arr, left, right):
    rand = randint(left, right)
    swap(arr, rand, right)
    i = left
    for j in range(left, right):
        if arr[j] <= arr[right]:
            swap(arr, i, j)
            i += 1
    swap(arr, i, right)
    return i


def select(A, p, k, r):
    if p == r: return A[p]
    while p < r:
        q = Partition(A, p, r)
        if q == k: return A[q]
        if q < k:
            return select(A, q + 1, k, r)
        else:
            return select(A, p, k, q - 1)


T = [1, 4, 3, 2]
print(select(T, 0, 3, len(T) - 1))