from SingleLinkedList import SingleLinkedList
from Node import Node

def deleteNodes(ll, m, n):
    if ll.head == None:
        return
    
    curr = ll.head
    count = 0 

    while curr:
        #loop through the m nodes
        for count in range(1, m):
            if curr is None:
                return
            curr = curr.next
        
        if curr is None:
            return
        
        #delete n nodes
        t = curr.next
        for count in range(1, n+1):
            if t is None:
                break
            t = t.next
        
        curr.next = t
        curr = t


    

    

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(4)
    n7 = Node(4)

    h = SingleLinkedList()

    h.insertNodeAtEnd(n1)
    h.insertNodeAtEnd(n2)
    h.insertNodeAtEnd(n3)
    h.insertNodeAtEnd(n4)
    h.insertNodeAtEnd(n5)
    h.insertNodeAtEnd(n6)
    h.insertNodeAtEnd(n7)

    h.printList()

    deleteNodes(h, 3, 6)

    print("========")
    h.printList()