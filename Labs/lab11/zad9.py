# Zadanie 2. Proszę zapropnować algorytm, który oblicza sumę wszystkich wartości
# w drzewie binarnym zdefiniowanym na węzłach typu:

class BNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.parent = None
        self.key = key

# Program może korzystać wyłącznie ze stałej liczby zmiennych (ale wolno mu zmieniać strukturę
# drzewa, pod warunkiem, że po zakończonych obliczeniach drzewo zostanie przywrócone do stanu początkowego.)

def MinElement(root):
    while root.left is not None: root = root.left
    return root.key

def MaxElement(root):
    while root.right is not None: root = root.right
    return root.key

def Find(root, key):
    while root is not None:
        if root.key == key: return root
        elif root.key < key: root = root.right
        else: root = root.left
    return None


def Successor(root): # następnik
    key = root.key
    element = Find(root, key)
    if element is None: return None # jeśli podany element nie istnieje to nie moze miec nastepnika
    if element.key == MaxElement(root): return None # jesli podany element jest najwiekszy to nie ma nastepnika

    if element.right is not None: return MinElement(element.right)

    while element.parent is not None:
        if element.parent.left == element: return element.parent.key
        element = element.parent

    return None

def Sum(root):
    root = MinElement(root)
    result = 0

    while root:
        result += root.key
        root = Successor(root)

    return result