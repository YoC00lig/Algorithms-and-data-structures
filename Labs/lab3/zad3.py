# Proszę zaimplementować algorytm QuickSort bez użycia rekurencji (ale można wykorzystać własny stos).

# ROZWIĄZANIE
# Nie można importować, więc skorzystam z własnej implementacji stosu w postaci pythonowej tablicy.

from random import randint

def Partition(arr,left,right):
    rand = randint(left,right)
    arr[rand], arr[right] = arr[right], arr[rand]
    i = left
    for j in range(left,right):
        if arr[j] <= arr[right]:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    arr[i], arr[right] = arr[right], arr[i]
    return i

def QuickSortIter(T):
    stack =[[0,len(T)-1]]
    while stack:
        left,right = stack.pop()
        if left < right:
            pivot = Partition(T,left,right)
            if pivot - left < right - pivot:
                stack.append([pivot+1,right])
                stack.append([left, pivot - 1])
            else:
                stack.append([left, pivot - 1])
                stack.append([pivot + 1, right])
    return T

def partition(T,p,k):
    l = p - 1
    for i in range(p,k):
        if T[i] < T[k]:
            l += 1
            T[i],T[l] = T[l], T[i]
    T[l+1], T[k] = T[k], T[l+1]
    return l + 1

def quicksortiter(A,p,k):

    T = []
    T.append((p,k))
    while T:
        p,k = T.pop()
        q = partition(A, p, k)
        if q-1 > p:
            T.append((p,q-1))
        if q+1 < k:
            T.append((q+1,k))
    return A

T = [1,-23,14,29,34,2,4,-1,0,76,3,-4]
print(QuickSortIter(T))