def CountingSort(T):
    tmp = [0] * len(T)
    counter = [0] * (max(T)+1)

    for i in range(len(T)):
        counter[T[i]] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    for i in range(len(T)-1, -1, -1):
        counter[T[i]] -= 1
        tmp[counter[T[i]]] = T[i]
    for i in range(len(T)):
        T[i] = tmp[i]

    return T