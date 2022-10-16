class Node():
    def __init__(self,val=0.0,next=None):
        self.val = val
        self.next = next


def insertionSortList(head):
    if head.next is None:
        return head
    start = Node()
    start.next = head
    prev = start
    curr = head
    while curr is not None:
        if curr.next is not None and curr.next.val < curr.val:
            # wstawianie
            while prev.next is not None and prev.next.val < curr.next.val:
                prev = prev.next

            tmp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = tmp
            prev = start

        else:
            curr = curr.next

    return start.next