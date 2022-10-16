"""
Given the head of a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees
of every node never differ by more than 1.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sortedListToBST(self, head):
    if not head: return
    if not head.next: return TreeNode(head.val)

    slow = head
    fast = head.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    tmp = slow.next
    slow.next = None
    root = TreeNode(tmp.val)
    root.right = self.sortedListToBST(tmp.next)
    root.left = self.sortedListToBST(head)
    return root