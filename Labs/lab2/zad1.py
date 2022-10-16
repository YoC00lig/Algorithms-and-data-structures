#Proszę zaimplementować:
#1. Scalanie dwóch posortowanych list jednokierunkowych do jednej.
#2. Algorytm sortowania list jednokierunkowych przez scalanie serii naturalnych.
#3. Co się stanie, jeśli w powyższym algorytmie będziemy łączyć poprzednio posortowaną listę z
# kolejną, zamiast łączenia dwóch kolejnych list?

class Node():
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

# ROZWIĄZANIE AD1
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

#ROZWIĄZANIE AD2

def cut_series(ll_head):
    if not ll_head: return None
    curr = ll_head
    while curr.next and curr.next.val >= curr.val:
        curr = curr.next
    remaining = curr.next
    curr.next = None
    return remaining


def mergesort(head):
    if head is None: return None
    tail = cut_series(head)
    start = head
    head = tail

    while head is not None:
        tail = cut_series(head)
        start = mergeTwoLists(start, head)
        head = tail

    return start