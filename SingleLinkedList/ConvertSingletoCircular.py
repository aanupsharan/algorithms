from SingleLinkedList import SingleLinkedList
from Node import Node

def convertSinglytoCircularList(ll):
    if ll.head == None:
        return
    
    curr = ll.head

    while curr.next != None :
        curr = curr.next
    
    print(curr)
    curr.next = ll.head

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

    h.printList()

    convertSinglytoCircularList(h)

    h.printList()

if __name__ == "__main__":
    main()