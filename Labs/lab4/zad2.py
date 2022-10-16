# Dana jest tablica A o długości n. Wartości w tablicy pochodzą ze zbioru B,
# gdzie ∣B∣ = log n. Proszę zaproponować możliwie jak najszybszy algorytm sortowania tablicy A.

# ROZWIĄZANIE
# tworzymy tablicę w której będziemy umieszczać logn unikatowych wartości.
# Do wyszukiwania, czy podana wartośc znajduje się już w tablicy wykorzystamy wyszukiwanie binarne.
# po każdym wstawieniu nowej unikalnej wartości musimy zadbać, aby niemalejący porządek w tablicy
# liczb unikalnych pozostał nienaruszony. Możemy do tego wykorzystać sortowanie proste, ponieważ tych
# liczb będzie logn, co finalnie w najgorszym przypadku da nam złożoność O(log^2 n).
# później zliczamy w tablicy count która liczba wystąpiła ile razy.

def BinarySearch(T, value):
    if T == []:
        return False
    left, right = 0, len(T) - 1
    while left <= right:
        mid = (left+right)//2
        if T[mid] == value:
            return mid
        elif T[mid] > value:
            right = mid - 1
        else:
            left = mid + 1
    return False

def insertion_sort(T):
    for i in range(1, len(T)):
        j = i - 1
        temp = T[i]
        while j >= 0 and temp < T[j]:
            T[j + 1] = T[j]
            j -= 1
        T[j + 1] = temp

def insertion(T,value):
    T.append(value)
    insertion_sort(T)

def SortLogN(T):
    unique = []
    for val in T:
        index = BinarySearch(unique,val)
        if index is False:
            insertion(T,val)

    count = [0]*len(unique)
    for val in T:
        index = BinarySearch(unique, val)
        count[index] += 1

    index = 0
    for i in range(len(unique)):
        for j in range(count[i]):
            T[index] = unique[i]
            index += 1
    return T