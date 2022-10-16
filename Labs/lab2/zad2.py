# Proszę zaproponować i zaimplementować algorytm, który mając na wejściu tablicę A zwraca
# liczbę jej inwersji (t.j., liczbę par indeksów i < j takich, że A[i] > A[j].

# ROZWIĄZANIE
# Do obliczania inwersji możemy wykorzystać algorytm Mergesort. W funkcji merge porównujemy dwie  części
# tablicy - lewą i prswą. jeśli w lewej tablicy element jest większy niż element z prawej oznacza to,
# że bieżąca wartość prawej tablicy jest w inwersji z każdą wartością z prawej tablicy począwszy od tej,
# z którą została ostatnio porównana, bo kolejne wartości w lewej tablicy są jeszcze większe(jest
# to tablica posortowana).

def mergesort(arr):
    n = len(arr)
    tmp_arr = [0 for _ in range(n)]
    return mergesort_algo(arr, tmp_arr, 0, n - 1)


def mergesort_algo(arr, tmp_arr, left, right):
    counter = 0
    if left < right:
        mid = (left + right) // 2
        counter += mergesort_algo(arr, tmp_arr, left, mid)
        counter += mergesort_algo(arr, tmp_arr, mid + 1, right)
        counter += merge(arr, tmp_arr, left, mid, right)
    return counter


def merge(arr, tmp_arr, left, mid, right):
    i = k = left
    j = mid + 1
    inv_count = 0

    while i <= mid and j <= right:
        if arr[i] <= arr[j]:
            tmp_arr[k] = arr[i]
            i += 1
        else:
            tmp_arr[k] = arr[j]
            j += 1
            inv_count += mid - i + 1
        k += 1

    while i <= mid:
        tmp_arr[k] = arr[i]
        k += 1
        i += 1
    while j <= right:
        tmp_arr[k] = arr[j]
        j += 1
        k += 1

    for q in range(left, right + 1):
        arr[q] = tmp_arr[q]

    return inv_count