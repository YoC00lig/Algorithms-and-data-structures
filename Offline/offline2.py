# Dany jest ciąg przedziałów domkniętych L = [[a1,b1],...,[an,bn]].
# Początki i końce przedziałów są liczbami naturalnymi.
# Poziomem przedziału c ∈ L nazywamy liczbę przedziałów w L, które w całości
# zawierają się w c (nie licząc samego c). Proszę zaproponować i zaimplementować algorytm,
# który zwraca maksimum z poziomów przedziałów znajdujących się w L.
# Proszę uzasadnić popraw- ność algorytmu i oszacować jego złożoność obliczeniową.
# Algorytm należy zaimplementować jako funkcję postaci:
    #def depth( L ):
      #...
# która przyjmuje listę przedziałów L i zwraca maksimum z poziomów przedziałów w L.
# Przykład. Dla listy przedziałów:
    #L = [ [1, 6],[5, 6],[2, 5],[8, 9],[1, 6]]
# wynikiem jest liczba 3.

# W zadaniu korzystam z algorytmu Quicksort.
# Na początku sortuję wszystkie przedziały po początkach.
# Następnie iteruje po tablicy i nadpisuję wartość każdego elementu
# tablicy nową tablicą w postaci: [początek przedziału, koniec przedziału,
# indeks przedziału w tablicy po posortowaniu].
# Tak przechowana informacja odnośnie położenia przedziału po posortowaniu przyda mi się
# w dalszej częsci zadania (ile przedziałów zaczyna się wcześniej od danego przedziału
# - tyle już nie może się całkowicie w nim zawierać).
# Później sortuję tablicę po końcach. Następnie na podstawie informacji,
# ile przedziałów zaczyna i kończy się wcześniej
# typuje przedział, który zawiera w sobie najwięcej innych przedziałów.
# W ostatniej pętli na potrzeby zadania dla tak znalezionego przedziału
# zliczam ile przedziałów faktycznie się w nim zawiera jednocześnie
# pamiętając aby nie był to ten sam przedział (i!=position).

#Złożoność obliczeniowa zaproponowanego algorytmu : 3*O(n) + 2*O(nlogn) ~= O(nlogn)

from random import randint
def partition(T, left, right,index):
    pivot_ind = randint(left, right)
    T[right], T[pivot_ind] = T[pivot_ind], T[right]
    i = left
    for j in range(left, right):
        if T[j][index] <= T[right][index]:
            T[i], T[j] = T[j], T[i]
            i += 1
    T[i], T[right] = T[right], T[i]
    return i

def quick_sort(T,p,k,index):
    while p<k:
        q = partition(T,p,k,index)
        if (q-p)>(k-q):
            quick_sort(T,q+1,k,index)
            k = q-1
        else:
            quick_sort(T,p,q-1,index)
            p = q + 1

def depth(L):
    n = len(L)
    included = position = result = 0

    quick_sort(L,0,n-1,0)
    for i in range(n):
        L[i] = [L[i][0],L[i][1],i]
    quick_sort(L,0,n-1,1)
    for i in range(n):
        if i-L[i][2] > included:
            included = i-L[i][2]
            position = i
    for i in range(n):
        if i != position and L[i][0] >= L[position][0] and L[i][1] <= L[position][1]:
            result += 1

    return result
