# Zadanie 5. (odwracanie listy) Proszę zaimplementować funkcję odwracającą listę jednokierunkową.

class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

def reverse(head):
    p = head.next
    prev = head
    prev.next = None
    while p is not None:
        m = p
        p = p.next
        m.next = prev
        prev = m
    new = Node()
    new = prev
    return new