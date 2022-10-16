# Proszę zaproponować algorytm scalający k posortowanych list.

# ROZWIĄZANIE 1 O(NlogK)
# Korzystamy z algorytmu łączenia dwóch posortowanych list i łączymy ze sobą po dwie listy do momentu,
# w którym otrzymamy jedną posortowaną listę

class Node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None and list2 is None:
        return None
    if list2 is None:
        return list1
    if list1 is None:
        return list2

    start = point = Node()
    while list1 and list2:
        if list1.val < list2.val:
            tmp = list1.next
            point.next = list1
            list1.next = None
            list1 = tmp
            point = point.next
        else:
            tmp = list2.next
            point.next = list2
            list2.next = None
            list2 = tmp
            point = point.next

    if list1 is None:
        point.next = list2
    elif list2 is None:
        point.next = list1

    result = start.next
    start.next = None
    del start
    return result

def MergekSortedLists(lists):
    interval = 1
    n = len(lists)
    if n == 0: return None
    while interval < n:
        for i in range(0, n - interval, 2 * interval):
            lists[i] = mergeTwoLists(lists[i], lists[i + interval])
        interval *= 2
    return lists[0]

# ROZWIĄZANIE 2 O(NlogK)
# korzystamy ze struktury kopca minimum
# ROZWIĄZANIE 2 O(NlogK)
# korzystamy ze struktury kopca minimum. Do kopca wstawiamy head i jego wartść dla każdej listy. Budujemy kopiec.
# Następnie tworzymy wartownika. z każdą iteracją wyjmujemy z kopca najmniejszą wartość i dopinamy do wynikowej listy.
# Następnie dodajemy do kopca następną wartość  z listy, z której wyjęliśmy minimum.
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

def Mergek(lists):
    start = point = Node()
    k = len(lists)
    heap = [[float('inf'), None] for _ in range(k)]
    ind = 0
    for i in range(k):
        if lists[i] is not None:
            heap[ind] = [lists[i].val, lists[i]]
            ind += 1
    buildheap(heap)

    while heap[0] != [float('inf'), None]:
        p = heap[0][1]
        point.next = p
        point=point.next
        if p.next is not None:
            heap[0] = [p.next.val, p.next]
        elif p.next is None:
            heap[0] = [float('inf'), None]
        Heapify(heap, len(heap), 0)

    result = start.next
    start.next = None
    del start
    return result