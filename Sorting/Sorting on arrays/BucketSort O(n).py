# O(n) dla danych z rozkładu jednostajnego
# Sortowanie kubełkowe

def InsertionSort(T):
    n = len(T)
    for i in range(1, n):
        j = i - 1
        key = T[i]
        while j >= 0 and key < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = key


def BucketSort(T):
    n = len(T)
    mini = min(T)
    maxi = max(T)
    interval = (maxi - mini) / n
    buckets = [[] for _ in range(n)]

    for val in T:  # wrzucam do odpowiedniego bucketa
        index = int((val - mini) / interval) if int((val - mini) / interval) < n else n - 1
        buckets[index].append(val)

    for bucket in buckets:  # sortuje każdy bucket
        InsertionSort(bucket)

    idx = 0
    for bucket in buckets:  # wpisuje element na odpowiednie miejsce w tablicy wejściowej
        if bucket != []:
            for elem in bucket:
                T[idx] = elem
                idx += 1
    return T


T = [0.4, 0.5, 0.34, 0.45, 0.56, 0.89, 0.67, 0.12, 0.68, 0.92, 0.59, 0.34]
print(BucketSort(T))