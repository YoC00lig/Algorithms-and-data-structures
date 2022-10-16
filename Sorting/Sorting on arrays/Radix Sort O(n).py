# sortowanie liczb

def CountingSort(T, col):
    tmp = [0] * len(T)
    counter = [0] * 10

    for i in range(len(T)):
        index = (T[i]//col) % 10
        counter[index] += 1
    for i in range(1, len(counter)):
        counter[i] += counter[i-1]
    for i in range(len(T)-1, -1, -1):
        index = (T[i]//col) % 10
        counter[index] -= 1
        tmp[counter[index]] = T[i]
    for i in range(len(T)):
        T[i] = tmp[i]

    return T

def RadixSort(T):
    div = 1
    maxi = max(T)
    while maxi // div != 0:
        CountingSort(T, div)
        div *= 10
    return T