# Mamy serię pojemników z wodą, połączonych (każdy z każdym) rurami. Pojemniki maja kształty prostokątów,
# rury nie maja objetosci (powierzchni). Każdy pojemnik opisany jest przez współrzędne lewego górnego
# rogu i prawego dolnego rogu.
# Wiemy, ze do pojemników nalano A “powierzchni” wody (oczywiście woda rurami spłynęła do najniźszych pojemników).
# Proszę zaproponować algorytm Obliczający ile pojemników zostało w pełni zalanych.


# Każdy kontener jest reprezentowany jako tupla
# container -> ((x1, y1), (x2, y2))
                #    |         |
                #left-top  right_bottom
# na początku sortujemy kontenerwy po ich górnej pozycji - jeśli górna pozycja jest niżej
# niż następnego kontenera, oznacza to że będzie on zalany wcześniej.
# jeśli kontenery kończą się na tej samej wysokości wybieramy ten, który zaczyna się na mniejszej wysokości.
# przy pomocy wyszukiwania binarnego badam na jakiej wysokości ile kontenerów zostałoby zapełnione i ile byłoby potrzebne wody.
def MergeSort(T):
    tmp = [None]*len(T)
    step = 1

    while step < len(T):
        for left in range(0,len(T)-step, 2*step):
            mid = left + step
            right = mid + step if mid + step <= len(T) else len(T)

            i = left
            j = mid
            k = left

            while i < mid and j < right:
                if T[i][0][1] < T[j][0][1] or (T[i][0][1] == T[j][0][1] and T[i][1][1] < T[j][1][1]):
                    tmp[k] = T[i]
                    i += 1
                else:
                    tmp[k] = T[j]
                    j += 1
                k += 1

            for i in range(i,mid):
                tmp[k] = T[i]
                k += 1
            for j in range(j,right):
                tmp[k] = T[j]
                k += 1

        for k in range(k, len(T)):
            tmp[k] = T[k]

        T, tmp = tmp, T
        step *= 2
    return T

# funkcja dla podanej wysokości bada, ile kontenerów zostałoby
# wypełnionych do tej wysokości i ile wody byłoby potrzebne
def FullContainersAtThisHeight(containers,height):
    capacity, fullContainers = 0, 0
    for container in containers:
        # kontener który jest powyżej tej wysokości nie jest brany pod uwagę
        if container[1][1] >= height: continue
        # kontener, który kończy się poniżej lub na tej wysokości zostanie całkowicie zalany
        if container[0][1] <= height:
            currHeight = container[0][1] - container[1][1]
            fullContainers += 1
        # kontener, który zaczyna się poniżej tej wysokości ale kończy
        # się powyżej. Jego część będzie napełniona, ale tylko do tej wysokości,
        # czyli nie liczymy tego do całkowicie pełnych kontenerów
        else: currHeight = height - container[1][1]

        currWidth = container[1][0] - container[0][0]
        capacity += currWidth*currHeight
    return capacity, fullContainers

def FullContainers(containers, water):
    if water <= 0: return
    containers = MergeSort(containers)
    # korzystamy z wyszukiwania binarnego do odnalezienia pełnej liczby kontenerów
    left = 0
    right = len(containers)-1
    while left <= right:
        mid = (left+right)//2
        top = containers[mid][0][1]
        requiredWater, fullcontainers = FullContainersAtThisHeight(containers, top)
        if water >= requiredWater: left = mid + 1
        else: right = mid - 1
    if right >= 0: _, fullcontainers = FullContainersAtThisHeight(containers, containers[right][0][1])
    else: fullcontainers = 0
    return fullcontainers