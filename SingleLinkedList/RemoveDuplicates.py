from SingleLinkedList import SingleLinkedList
from Node import Node

def removeDuplicatesFromSortedList(ll):
    if ll.head == None:
        return
    prev, curr = ll.head, ll.head.next
    while curr != None:
        if prev.val == curr.val:
            prev.next = curr.next
            curr.next = None
            curr = prev.next
        else:
            curr = curr.next
            prev = prev.next

def main():
    n1 = Node(1)
    n2 = Node(2)
    #n3 = Node(2)
    #n4 = Node(3)
    #n5 = Node(4)
    #n6 = Node(4)
    #n7 = Node(4)
    #n8 = Node(5)
    #n9 = Node(5)

    h = SingleLinkedList()

    h.insertNodeAtEnd(n1)
    h.insertNodeAtEnd(n2)
    #h.insertNodeAtEnd(n3)
    #h.insertNodeAtEnd(n4)
    #h.insertNodeAtEnd(n5)
    #h.insertNodeAtEnd(n6)
    #h.insertNodeAtEnd(n7)
    #h.insertNodeAtEnd(n8)
    #h.insertNodeAtEnd(n9)

    h.printList()

    removeDuplicatesFromSortedList(h)

    h.printList()

if __name__ == "__main__":
    main()