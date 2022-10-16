def partition(arr, left, right):
    rand_index = left
    arr[right], arr[rand_index] = arr[rand_index], arr[right]
    i = left
    for j in range(left, right):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def quicksort(arr, left, right):
    while left < right:
        pivot = partition(arr, left, right)
        if pivot - left < right - pivot:
            quicksort(arr, left, pivot - 1)
            left = pivot + 1
        else:
            quicksort(arr, pivot + 1, right)
            right = pivot - 1
    return arr

def quick_sort(arr):
    return quicksort(arr, 0, len(arr) - 1)