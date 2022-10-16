# Zadanie 2. (następnik) Proszę zaimplementować funkcję znajdującą element o następnej
# wartości klucza niż podany w drzewie BST

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None


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

def Successor(root, key): # następnik
    element = Find(root, key)
    if element is None: return None # jeśli podany element nie istnieje to nie moze miec nastepnika
    if element.key == MaxElement(root): return None # jesli podany element jest najwiekszy to nie ma nastepnika

    if element.right is not None: return MinElement(element.right)

    while element.parent is not None:
        if element.parent.left == element: return element.parent.key
        element = element.parent

    return None

def Predecessor(root, key):
    element = Find(root, key)
    if element is None: return None  # jeśli podany element nie istnieje to nie moze miec poprzednika
    if element.key == MinElement(root): return None  # jesli podany element jest najmniejszy to nie ma poprzednika

    if element.left is not None: return MaxElement(element.left)

    while element.parent is not None:
        if element.parent.right == element: return element.parent.key
        element = element.parent

    return None

a = BSTNode(10)
b = BSTNode(5)
c = BSTNode(20)

a.left = b
a.right = c
c.parent=b.parent=a

d = BSTNode(4)
b.left = d
d.parent = b

e = BSTNode(15)
f = BSTNode(25)
c.left = e
c.right = f
e.parent = f.parent = c

g = BSTNode(12)
e.left = g
g.parent = e


h = BSTNode(22)
i = BSTNode(27)

h.parent = i.parent = f
f.left = h
f.right = i

j = BSTNode(21)
k = BSTNode(24)

h.left = j
h.right = k
j.parent=k.parent=h
print(Successor(a, 4))





