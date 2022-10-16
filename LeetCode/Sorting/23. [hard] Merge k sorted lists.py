"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.


"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeKLists(lists):
    def mergeTwoLists(list1, list2):
        if list1 is None and list2 is None:
            return None
        if list2 is None:
            return list1
        if list1 is None:
            return list2

        start = point = ListNode()
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

    def MergekSortedLists(lists):
        interval = 1
        n = len(lists)
        if n == 0:
            return None
        while interval < n:
            for i in range(0, n - interval, 2 * interval):
                lists[i] = mergeTwoLists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0]


    return MergekSortedLists(lists)