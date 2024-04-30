from SingleLinkedList import SingleLinkedList
from Node import Node

def deleteLastOccurence(head, key):
    if head == None:
        return
    
    temp = head
    keyNode = None    
    while temp != None:
        if temp.val == key:
            keyNode = temp
        temp = temp.next

    temp = head
    #if key node is the last node of the list
    if keyNode != None and keyNode.next == None:
        while temp != keyNode:
            temp = temp.next
        temp.next = None
        return head
    
    if keyNode != None and keyNode.next != None:
       keyNode.data = keyNode.next.data
       temp = keyNode.next
       keyNode.next = temp.next
       temp.next = None
       return head


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

    h.head = deleteLastOccurence(h.head, 4)

    print("========")
    h.printList()
