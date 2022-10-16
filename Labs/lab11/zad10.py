# Zadanie 3. (geny) W pewnym laboratorium genetycznym powstał ciąg sekwencji DNA. Każda sekwencja
# to pewien napis składający się z symboli G, A, T, i C. Przed dalszymi badaniami konieczne jest
# upewnić się, że wszystkie sekwencje DNA są parami różne. Proszę opisać algorytm, który sprawdza
# czy tak faktycznie jest.



# Tworzę drzewo, gdzie z każdego wierzchołka wychodzą 4 inne wierzchołki odpowiadające literom G,A,T,C.
# dodatkowo przechowuje w każdym wierzchołku informację dotyczącą tego, czy któraś sekwencja kończy się w tym wierzchołku.

class Node:
    def __init__(self):
        self.G = None
        self.A = None
        self.T = None
        self.C = None
        self.end = False

def Check(root, sequence, i):
    if i == len(sequence):
        if root.end: return False # jeśli dotarliśmy do końca sekwencji i okazuje sie, że któreś słowo już się kończy w tym miejscu, to znaczy że istnieje już taka sekwencja
        root.end = True
        return True

    if sequence[i] == "G":
        if root.G is None: root.G = Node()
        return Check(root.G, sequence, i + 1)

    elif sequence[i] == "A":
        if root.A is None: root.A = Node()
        return Check(root.A, sequence, i + 1)

    elif sequence[i] == "T":
        if root.T is None: root.T = Node()
        return Check(root.T, sequence, i + 1)

    elif sequence[i] == "C":
        if root.C is None: root.C = Node()
        return Check(root.C, sequence, i + 1)

def CheckDifference(gens):
    root = Node()

    for sequence in gens:
        if not Check(root, sequence, 0): return False

    return True