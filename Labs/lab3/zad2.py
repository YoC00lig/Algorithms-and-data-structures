# Proszę zaimplementować funkcję wstawiającą dowolny element do kopca binarnego.

# ROZWIĄZANIE
# Na początku dodajemy element do tablicy reprezentującej kopiec na sam koniec.
# Następnie w pętli odwołujemy się do rodzica danego elementu i porównujemy, czy jest on większy.
# Jeśli tak to zamieniamy je miejscem i pniemy się w kopcu "do góry" i sprawdzamy kolejną parę dziecko-rodzic.
# Pętlę przerywamy jeśli dojdziemy do szczytu kopca lub kiedy rodzic będzie większy od porównywanego elementu.

def left(i):
    return 2 * i + 1

def right(i):
    return 2 * i + 2

def parent(i):
    return (i - 1) // 2

def addtoheap(heap,elem):
    heap.append(elem)
    n = len(heap) - 1
    while True:
        par = parent(n)
        if heap[par] < heap[n]:
            heap[par], heap[n] = heap[par], heap[par]
            n = par
        elif n == 0: break
        else: break