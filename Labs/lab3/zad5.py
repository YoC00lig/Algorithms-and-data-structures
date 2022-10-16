# Proszę przedstawić W jaki sposób zrealizować strukturę danych, która pozwala wykonywać operacje"
# 1.Insert
# 2.RemoveMin
# 3.RemoveMax
# tak, żeby wszystkie operacje działały w czasie O(logn)

# ROZWIĄZANIE
# Utworzę dwa kopce, jeden kopiec minimum i drugi kopiec maksimum, które będą przechowywały takie same dane.
# Usuwanie minimum z kopca minimum i maksimum z kopca maksimum oraz dodanie elementu działają w czasie
# jednostkowym, natomiast po kazdej z tych operacji musimy przywrócić własność kopca O(logn).
# Problem pojawia się w momencie, w którym musimy usunąć minimum z kopca maksimum lub maksimum z kopca minimum.
# Problem ten rozwiążę w taki sposób, że każdy element z jednego kopca będzie posiadał swoją referencję
# do siebie w drugim kopcu.

class Reference:
    def __init__(self,value=None):
        self.value = value
        self.minHeap = None
        self.maxHeap = None

def left(i):
    return 2 * i + 1
def right(i):
    return 2 * i + 2
def parent(i):
    return (i - 1) // 2

def HeapifyMin(heap, nextIndex, start=0):
    end = nextIndex
    l = left(start)
    r = right(start)
    minIND = start
    if l < end and heap[l].value < heap[minIND].value:
        minIND = l
    if r < end and heap[r].value < heap[minIND].value:
        minIND = r
    if minIND != start:
        heap[start].minHeap = minIND
        heap[minIND].minHeap = start
        heap[start], heap[minIND] = heap[minIND], heap[start]
        HeapifyMin(heap,nextIndex,minIND)

def buildheapMIN(heap):
    n = len(heap)
    for i in range(parent(n - 1), -1, -1):
        HeapifyMin(heap, n, i)
    for j in range(n):
        heap[j].minHeap = j
    return heap

def HeapifyMax(heap, nextIndex, start=0):
    end = nextIndex
    l = left(start)
    r = right(start)
    maxIND = start
    if l < end and heap[l].value > heap[maxIND].value:
        maxIND = l
    if r < end and heap[r].value > heap[maxIND].value:
        maxIND = r
    if maxIND != start:
        heap[start].maxHeap = maxIND
        heap[maxIND].maxHeap = start
        heap[start], heap[maxIND] = heap[maxIND], heap[start]
        HeapifyMax(heap,nextIndex,maxIND)

def buildheapMAX(heap):
    n = len(heap)
    for i in range(parent(n - 1), -1, -1):
        HeapifyMax(heap, n, i)
    for j in range(n):
        heap[j].maxHeap = j
    return heap

def addtoheapMAX(heap,elem):
    heap.append(elem)
    n = len(heap) - 1
    while True:
        par = parent(n)
        if heap[par] < heap[n]:
            heap[par].maxHeap = n
            heap[n].maxHeap = par
            heap[par],heap[n] = heap[n], heap[par]
            n = par
        elif n == 0:
            break
        else:
            break

def addtoheapMIN(heap,elem):
    heap.append(elem)
    n = len(heap) - 1
    while True:
        par = parent(n)
        if heap[par] > heap[n]:
            heap[par].minHeap = n
            heap[n].minHeap = par
            heap[par],heap[n] = heap[n], heap[par]
            n = par
        elif n == 0:
            break
        else:
            break

def Insert(maxHeap,minHeap,val):
    TOADD = Reference(value=val)
    addtoheapMIN(minHeap,TOADD)
    addtoheapMAX(maxHeap,TOADD)

def RemoveMax(maxheap,minheap):
    last = maxheap.pop()
    biggest = maxheap[0]
    maxheap[0] = last
    maxheap[0].maxHeap = 0
    HeapifyMax(maxheap,len(maxheap),0)

    mini = biggest.minHeap
    last = minheap.pop()
    if mini == len(minheap): return #it was last
    minheap[mini] = last
    minheap[mini].minHeap = mini
    while True:
        par = parent(mini)
        if minheap[par] > minheap[mini]:
            minheap[par].minHeap = mini
            minheap[mini].minHeap = par
            minheap[par], minheap[mini] = minheap[mini], minheap[par]
            mini = par
        elif mini == 0:
            break
        else:
            break
def RemoveMin(maxheap,minheap):
    last = minheap.pop()
    smallest = minheap[0]
    minheap[0] = last
    minheap[0].minHeap = 0
    HeapifyMin(minheap,len(minheap),0)

    maxi = smallest.maxHeap
    last = maxheap.pop()
    if maxi == len(maxheap): return #it was last
    maxheap[maxi] = last
    maxheap[maxi].maxHeap = maxi
    while True:
        par = parent(maxi)
        if maxheap[par] > maxheap[maxi]:
            maxheap[par].maxHeap = maxi
            maxheap[maxi].maxHeap = par
            maxheap[par], maxheap[maxi] = maxheap[maxi], maxheap[par]
            maxi = par
        elif maxi == 0:
            break
        else:
            break