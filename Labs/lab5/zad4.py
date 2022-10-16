# Zadanie 4. (najdłuższy podciąg rosnący) Proszę rozwiązać dwa następujące zadania:
# 1. Jak wykorzystać algorytm dla problemu najdłuższego wspólnego podciągu do rozwiązania zadania
# najdłuższego rosnącego podciągu?
# 2. Na wykładzie podaliśmy algorytm działający w czasie O (n2). Proszę podać algorytm o złożoności
# O (nlog n).

# AD1 - tworzymy drugą tablicę, która będzie zawierała te same elementy.
# Następnie ją sortujemy i szukamy najdłuższego wspólnego podciągu w obydwu tablicach.
def LongestCommonSubsequence(A, B):
    n = len(A)
    matrix = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        if B[i] == A[0]:
            matrix[0][i] = 1
        if B[0] == A[i]:
            matrix[i][0] = 1

    for a in range(1, n):
        for b in range(1, n):
            if A[a] == B[b]:
                matrix[a][b] = matrix[a - 1][b - 1] + 1
            else:
                matrix[a][b] = max(matrix[a - 1][b], matrix[a][b - 1])

    return matrix[-1][-1]

from copy import deepcopy
def LisUsingLcs(T):
    S = deepcopy(T)
    S.sort()
    return LongestCommonSubsequence(S,T)

# AD 2 LIS O (nlog n)
# Wyszukiwanie binarne pomoże odnaleźć miejsce, na którym powinna się znaleźć dana liczba w posortowanej tablicy.
def BinarySearch(T,number,start,end):
    left  = start
    right = end
    while left <= right:
        mid = (left+right)//2
        if T[mid] == number:
            return mid # czy to potrzebne?
        elif T[mid] < number:
            left = mid + 1
        else:
            right = mid - 1
    return left

def LongIncSub1(T):
    lenght = 1
    n = len(T)
    result = [0 for _ in range(n)]
    result[0] = T[0]
    for i in range(1,n):
        if T[i] > result[lenght-1]:
            result[lenght] = T[i]
            lenght += 1
        elif T[i] < result[0]:
            result[0] = T[i]
        else:
            index = BinarySearch(result,T[i],0,lenght-1)
            result[index] = T[i]
    return lenght

# Dodatkowo LIS O(n^2)
def LIS(A):
    n = len(A)
    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                F[i] = F[j] + 1

    return max(F)
