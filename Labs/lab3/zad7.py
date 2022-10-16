# Proszę zaimplementować funkcję partition z algorytmu QuickSort według pomysłu
# Hoare’a (tj. mamy dwa indeksy, i oraz j, wędrujące z obu końców tablicy w stronę środka
# i zamieniamy elementy tablicy pod nimi jeśli mniejszy indeks wskazuje na wartość większą
# od piwota, a większy na mniejszą.

def _partition(arr, left, right):
    pivot = arr[left]
    i = left - 1
    j = right + 1
    while True:
        i += 1
        while arr[i] < pivot: i += 1

        j -= 1
        while arr[j] > pivot: j -= 1

        if i < j:arr[i], arr[j] = arr[j], arr[i]
        else: return j


def quicksort(arr, left, right):
    while left < right:
        pivot = _partition(arr, left, right)
        if pivot - left < right - pivot:
            quicksort(arr, left, pivot)
            left = pivot + 1
        else:
            quicksort(arr, pivot+1, right)
            right = pivot
    return arr

def quick_sort(arr):
    quicksort(arr, 0, len(arr) - 1)

T = [-2,10,0,2,5,3,-23,890,-5,2,11,100]
quick_sort(T)
print(T)
