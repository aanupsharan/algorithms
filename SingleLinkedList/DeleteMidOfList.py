from SingleLinkedList import SingleLinkedList
from Node import Node

def deleteMidOfList(ll):
    if ll.head == None or ll.head.next == None:
        return ll
    
    prev, curr = None, ll.head
    len = ll.lengthOfList()
    mid = round(len/2)

    while mid:
        prev = curr
        curr = curr.next
        mid -= 1
    prev.next = curr.next
    curr.next = None

    return ll

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)

    h = SingleLinkedList()

    h.insertNodeAtEnd(n1)
    h.insertNodeAtEnd(n2)
    h.insertNodeAtEnd(n3)
    h.insertNodeAtEnd(n4)
    h.insertNodeAtEnd(n5)

    q = deleteMidOfList(h)

    q.printList()

if __name__ == "__main__":
    main()