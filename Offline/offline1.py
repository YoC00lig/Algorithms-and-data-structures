# Węzły jednokierunkowej listy odsyłaczowej reprezentowane są w postaci:
class Node:
    def __init__(self):
        self.val  = None  # przechowywana liczba rzeczywista
        self.next = None  # odsyłacz do nastepnego elementu

# Niech p będzie wskaźnikiem na niepustą listę odsyłaczową zawierającą parami różne liczby rzeczywiste a1,a2,...,an
# (lista nie ma wartownika). Mówimy, że lista jest k-chaotyczna jeśli dla każdego elementu zachodzi,
# że po posortowaniu listy znalazłby się na pozycji różniącej się od bieżącej o najwyżej k.
# Tak więc 0-chaotyczna lista jest posortowana, przykładem 1-chaotycznej listy jest 1,0,3,2,4,6,5,
# a (n−1)-chaotyczna lista długości n może zawierać liczby w dowolnej kolejności. Proszę zaimplementować
# funkcję SortH(p,k), która sortuje k-chaotyczną listę wskazywaną przez p. Funkcja powinna zwrócić
# wskazanie na posortowaną listę. Algorytm powinien być jak najszybszy oraz używać jak najmniej pamięci
# (w sensie asymptotycznym, mierzonym względem długości n listy oraz parametru k).
# Proszę skomentować jego złożoność czasową dla k = Θ(1), k = Θ(logn) oraz k = Θ(n).


# W algorytmie wykorzystuję strukturę danych - kopiec minimum o rozmiarze k+1.
# na początku tworzę wartownika, który  pomoże mi w przepinaniu listy.
# W pierwszej pętli wypełniam tablicę heap pierwszymi k+1 wartościami
# z listy w postaci [wartość elementu listy, wskaźnik na element listy].
# Następnie korzystając z funkcji buildheap buduję kopiec minimum.
# W drugiej pętli iteruje przez całą listę. W każdej iteracji usuwam pierwszy element z kopca, który jest
# minimum i przypinam go do wynikowej listy jako kolejny element.
# Następnie na jego miejsce w kopcu  wstawiam kolejny element z listy i naprawiam kopiec.
# W ostatniej pętli sprawdzam czy kopiec jest już pusty. Jeśli nie, to wyjmuje z niego pozostałe wartości
# jednocześnie za każdym razem naprawiając kopiec.
# Na samym końcu algorytmu odpinam z wynikowej listy i usuwam wartownika

# Złożoność czasowa algorytmu to: O(nlog(k+1))

# dla k = O(1) złożoność - O(nlog2)
# dla k = O(logn) złożoność - O(nlog(logn))
# dla k = O(n) złożoność O(nlogn)

def parent(i):
    return (i - 1) // 2

def left(i):
    return (i * 2) + 1

def right(i):
    return (i * 2) + 2

def Heapify(heap, nextIndex, start=0):
    end = nextIndex
    l = left(start)
    r = right(start)
    minIND = start
    if l < end and heap[l] is not None and heap[l][0] < heap[minIND][0]:
        minIND = l
    if r < end and heap[r] is not None and heap[r][0] < heap[minIND][0]:
        minIND = r
    if minIND != start:
        heap[start], heap[minIND] = heap[minIND], heap[start]
        Heapify(heap,nextIndex,minIND)

def buildheap(heap):
    n = len(heap)
    for i in range(parent(n - 1), -1, -1):
        Heapify(heap, n, i)

def SortH(p,k):
    if k <= 0: return p
    start = w = Node()
    point = p
    heap = [None] * (k+1)
    index = 0


    while point and index < k + 1:
        heap[index] = [point.val, point]
        index += 1
        point = point.next

    buildheap(heap)

    while point:
        mini = heap[0][1]
        w.next = mini
        w = mini
        heap[0] = [point.val, point]
        point = point.next
        Heapify(heap,len(heap),0)

    while heap[0][1] is not None:
        mini = heap[0][1]
        w.next = mini
        w = mini
        heap[0] = [float('inf'), None]
        Heapify(heap, len(heap), 0)

    w.next = None
    tmp = start
    start = start.next
    tmp.next = None
    del tmp
    return start

