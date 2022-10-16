# LIS O(nlog n)
# Wyszukiwanie binarne pomoże odnaleźć miejsce, na którym powinna się znaleźć dana liczba w posortowanej tablicy.
def BinarySearch(T,number,start,end):
    left = start
    right = end
    while left <= right:
        mid = (left+right)//2
        if T[mid] <= number:
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

# LIS O(n^2)
def LIS(A):
    n = len(A)
    F = [1] * n

    for i in range(1, n):
        for j in range(i):
            if A[j] < A[i] and F[i] < F[j] + 1:
                F[i] = F[j] + 1

    return max(F)
