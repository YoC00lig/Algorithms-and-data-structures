class Node():
    def __init__(self,val=0.0,next=None):
        self.val = val
        self.next = next

def insertionSortList(head):
    if head is None or head.next is None: return head
    start = Node()
    start.next = head
    prev = start
    curr = head
    while curr is not None:
        if curr.next is not None and curr.next.val < curr.val:
            # robimy wstawianie
            while prev.next is not None and prev.next.val < curr.next.val:
                prev = prev.next

            tmp = prev.next
            prev.next = curr.next
            curr.next = curr.next.next
            prev.next.next = tmp
            prev = start

        else:
            curr = curr.next

    while prev.next!= None:
        prev = prev.next

    return start.next

def minimax(head):
    p = head
    mini=maxi=p.val
    while p:
        if p.val > maxi:
            maxi = p.val
        if p.val < mini:
            mini = p.val
        p = p.next
    return mini,maxi

def lenght(head):
    l = 0
    p = head
    while p:
        l += 1
        p= p.next
    return l

def findTail(head):
    p = head
    while p.next!=None:
        p=p.next
    return p

def BucketSort(head):
    if lenght(head) < 2: return
    mini,maxi = minimax(head)
    k = maxi - mini
    n = lenght(head)
    interval = k/n
    buckets = [[None, None] for _ in range(n)]
    curr = head
    while curr:
        index = int((curr.val - mini)/interval) if int((curr.val - mini)/interval) < n else n -1
        tail = buckets[index][1]
        if tail == None:
            tmp = curr.next
            curr.next = None
            buckets[index][1] = curr
            buckets[index][0] = curr
            curr = tmp

        else:
            tmp = curr.next
            curr.next = None
            buckets[index][1].next = curr
            curr = tmp

    for i in range(len(buckets)):
        if buckets[i][0] != None:
            start = insertionSortList(buckets[i][0])
            end = findTail(start)
            buckets[i] = [start,end]

    sentinel = node = Node()
    for i in range(len(buckets)):
        if buckets[i][0] != None:
            node.next = buckets[i][0]
            node = buckets[i][1]

    res = sentinel.next
    sentinel.next =None
    del sentinel
    return res