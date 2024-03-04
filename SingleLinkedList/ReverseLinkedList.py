from SingleLinkedList import SingleLinkedList
from Node import Node

def reverseSingleLinkedList(ll):
    if ll.head == None or ll.head.next == None:
        return
    curr, nex, prev = ll.head, ll.head, None
    while curr != None:
        nex = curr.next
        curr.next = prev
        prev = curr
        curr = nex
    ll.head = prev

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    #n4 = Node(4)
    #n5 = Node(5)

    h = SingleLinkedList()

    h.insertNodeAtEnd(n1)
    h.insertNodeAtEnd(n2)
    h.insertNodeAtEnd(n3)
    #h.insertNodeAtEnd(n4)
    #h.insertNodeAtEnd(n5)

    h.printList()

    reverseSingleLinkedList(h)

    h.printList()

if __name__ == "__main__":
    main()