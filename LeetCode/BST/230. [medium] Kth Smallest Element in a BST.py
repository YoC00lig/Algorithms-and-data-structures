"""
Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the
values of the nodes in the tree.
"""


def kthSmallest(root, k):
    stack = []

    while True:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        k -= 1
        if not k:
            return root.val
        root = root.right