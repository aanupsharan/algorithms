from SingleLinkedList import SingleLinkedList
from Node import Node

def pairwiseSwap(list):
    if list.head == None or list.head.next == None:
        return list
    
    noOfNodes = list.lengthOfList()
    noOfSwaps = round(noOfNodes/2) - 1
    p = list.head
    q = list.head.next

    for x in range(noOfSwaps):
        p.next = q.next
        q.next = p
        if x == 0:
            list.head = q
        p = p.next
        q = p.next
    return list



if __name__ == "__main__":
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

    r = pairwiseSwap(h)

    r.printList()