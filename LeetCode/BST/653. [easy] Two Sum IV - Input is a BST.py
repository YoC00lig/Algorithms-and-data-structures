"""
Given the root of a Binary Search Tree and a target number k, return true if there exist two elements in the BST such that their sum is equal to the given target.


"""


def findTarget(root,k):
    def pushLeft(st, root):
        while root:
            st.append(root)
            root = root.left

    def pushRight(st, root):
        while root:
            st.append(root)
            root = root.right

    def nextLeft(st):
        node = st.pop()
        pushLeft(st, node.right)
        return node.val

    def nextRight(st):
        node = st.pop()
        pushRight(st, node.left)
        return node.val

    l, r = [], []
    pushLeft(l, root)
    pushRight(r, root)
    left, right = nextLeft(l), nextRight(r)

    while left < right:
        if left + right == k:
            return True
        elif left + right > k:
            right = nextRight(r)
        else:
            left = nextLeft(l)
    return False