class Node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

def mergeTwoLists(list1, list2):
    if list1 is None and list2 is None:
        return None
    if list2 is None:
        return list1
    if list1 is None:
        return list2

    start = point = Node()
    while list1 and list2:
        if list1.val < list2.val:
            tmp = list1.next
            point.next = list1
            list1.next = None
            list1 = tmp
            point = point.next
        else:
            tmp = list2.next
            point.next = list2
            list2.next = None
            list2 = tmp
            point = point.next

    if list1 is None:
        point.next = list2
    elif list2 is None:
        point.next = list1

    result = start.next
    start.next = None
    del start
    return result

def getMiddle(head):
    if head is None or head.next is None: return head
    slow = fast = head
    while fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    return slow

def MergeSort(head):
    if not head or not head.next: return head
    mid = getMiddle(head)
    nexttomid = mid.next
    mid.next = None
    left = MergeSort(head)
    right = MergeSort(nexttomid)
    result = mergeTwoLists(left, right)
    return result