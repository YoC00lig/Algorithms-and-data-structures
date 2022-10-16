def MergeSort(T):
    tmp = [None]*len(T)
    step = 1

    while step < len(T):
        for left in range(0, len(T)-step, 2*step):
            mid = left + step
            right = mid + step if mid + step <= len(T) else len(T)

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if T[i] <= T[j]:
                    tmp[k] = T[i]
                    i += 1
                else:
                    tmp[k] = T[j]
                    j += 1
                k += 1

            for i in range(i, mid):
                tmp[k] = T[i]
                k += 1
            for j in range(j, right):
                tmp[k] = T[j]
                k += 1

        for k in range(k, len(T)):
            tmp[k] = T[k]

        T, tmp = tmp, T
        step *= 2
    return T