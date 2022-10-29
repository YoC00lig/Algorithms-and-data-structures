from kol1atesty import runtests

def CountingSort(T,ind):
    n = len(T)
    cnt = [0] * 27
    tmp = [0] * n
    for i in range(n):
        index = ord(T[i][ind]) - 97
        cnt[index] += 1
    for i in range(1,27):
        cnt[i] += cnt[i-1]
    for i in range(n):
        index = ord(T[i][ind]) - 97
        cnt[index] -= 1
        tmp[cnt[index]] = T[i]
    for i in range(n):
        T[i] = tmp[i]

def RadixSort(T,maxlen):
    for i in range(maxlen-1,-1,-1):
        CountingSort(T,i)

def normalize(word):
    sec = word[::-1]
    if ord(sec[0]) < ord(word[0]): return sec
    return word

def GetAns(bucket):
    maxi = 0
    curr = bucket[0]
    cnt = 1

    for i in range(1,len(bucket)):
        if bucket[i] == curr:
            cnt += 1
            if cnt > maxi: maxi = cnt
        else:
            curr = bucket[i]
            cnt = 1
    return maxi

def g(T):
    maxi = None
    n = len(T)
    for i in range(n):
        if maxi is None or len(T[i]) > maxi:
            maxi = len(T[i])

    buckets = [[] for _ in range(maxi + 1)]
    for i in range(n):
        index = len(T[i])
        normalized = normalize(T[i])
        buckets[index].append(normalized)

    for i in range(len(buckets)):
        if buckets[i] != []:
            RadixSort(buckets[i], i)

    max_cnt = 0
    for bucket in buckets:
        if bucket!=[]:
            ans = GetAns(bucket)
            if ans > max_cnt: max_cnt = ans

    return max_cnt


# Zamien all_tests=False na all_tests=True zeby uruchomic wszystkie testy
runtests( g, all_tests=True )

