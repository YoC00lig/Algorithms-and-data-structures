# Zadanie 1. (Indeksowane drzewa BST) Rozważmy drzewa BST, które dodatkowo w każdym węźle zawierają
# pole z liczbą węzłów w danym poddrzewie. Proszę opisać jak w takim drzewie wykonywać następujące operacje:

# 1. znalezienie i-go co do wielkości elementu,
# 2. wyznaczenie, którym co do wielkości w drzewie jest zadany węzeł

# Proszę zaimplementować obie operacje.

class BSTNode:
    def __init__(self, key):
        self.key = key
        self.parent = None
        self.right = None
        self.left = None
        self.num = 1 # liczba węzłów w danym poddrzewie


def insert(root, node): # wstawianie do drzewa BST z indeksowaniem
    p = root # parent

    while root is not None:

        root.num += 1
        if root.key < node.key: p, root = root, root.right
        elif root.key > node.key: p, root = root, root.left

    if p.key > node.key: p.left = node
    else: p.right = node

    node.parent = p
    return node



# Na początku sprawdzam ilość węzłów z lewej strony - jest to ilośc najmniejszych liczbw drzewie.
# jeśli ilość tych mniejszych liczb plus jeden jest równa szukanemu indeksowi to znaczy, że szukanym elementem jest korzeń.
# Jeśli ilość elementów z lewej strony jest większa bądź równa indeksowi to szukamy w lewym poddrzewie - w przeciwnym razie w prawym.

def ad1(root, index):
    while True:
        leftV = root.left.num if root.left is not None else 0
        if leftV + 1 == index: return root.key

        if root.left is not None and root.left.num >= index: root = root.left
        else:
            index -= leftV + 1
            root = root.right

# lub stos
def kthSmallest(root, k):
    stack = []
    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k: return root.val
        root = root.right


# początkowo indeks jest równy tyle, ile jest mniejszych elementów .
# później wspinam się po drzewie do góry, jeśli przychodzę do parenta jako prawe dziecko to znaczy, że parent i lewe
# poddrzewo parenta to mniejsze elementy.

def ad2(node):
    index = node.left.num if node.left else 1

    while node.parent:
        if node == node.parent.right:
            index += node.parent.left.num if node.parent.left else 0
            index += 1
        node = node.parent

    return index



A = BSTNode(7)
insert(A, BSTNode(20))
insert(A, BSTNode(3))
insert(A, BSTNode(1))
insert(A, BSTNode(6))
insert(A, BSTNode(18))
b=insert(A, BSTNode(21))
insert(A, BSTNode(23))
