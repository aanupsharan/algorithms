from SingleLinkedList import SingleLinkedList
from Node import Node

def deleteFromEnd(ll, k):
    if ll.head == None:
        return ll
    
    len = ll.lengthOfList()
    if len < k:
        return ll

    position = len-k+1
    prev, curr = None, ll.head
    
    while position > 1:
        prev = curr
        curr = curr.next
        position -= 1

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

    q = deleteFromEnd(h, 2)

    q.printList()

if __name__ == "__main__":
    main()