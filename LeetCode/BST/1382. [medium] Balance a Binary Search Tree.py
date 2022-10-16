"""
Given the root of a binary search tree, return a balanced binary search tree with the same node values. If there is more than one answer, return any of them.

A binary search tree is balanced if the depth of the two subtrees of every node never differs by more than 1.


"""

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right


def balanceBST(root):
    nodes = []

    def inorder(root):
        if root is None: return
        inorder(root.left)
        nodes.append(root)
        inorder(root.right)

    def build(left, right):
        if left > right: return None
        mid = (left + right) // 2
        root = nodes[mid]
        root.left = build(left, mid - 1)
        root.right = build(mid + 1, right)
        return root

    inorder(root)
    return build(0, len(nodes) - 1)