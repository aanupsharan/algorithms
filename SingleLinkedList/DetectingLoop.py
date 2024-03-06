from SingleLinkedList import SingleLinkedList
from Node import Node

def isLoopInList(ll):
    if ll.head == None:
        return False

    slow = ll.head
    fast = ll.head.next

    while slow != None and fast != None:
        if slow is fast:
            return True

        slow = slow.next
        fast = fast.next.next
    
    return False

def main():
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n4 = Node(4)
    n5 = Node(5)
    n6 = Node(6)
    n7 = Node(7)
    n8 = Node(8)
    n9 = Node(9)

    h = SingleLinkedList()

    h.insertNodeAtEnd(n1)
    h.insertNodeAtEnd(n2)
    h.insertNodeAtEnd(n3)
    h.insertNodeAtEnd(n4)
    h.insertNodeAtEnd(n5)
    h.insertNodeAtEnd(n6)
    h.insertNodeAtEnd(n7)
    h.insertNodeAtEnd(n8)
    h.insertNodeAtEnd(n9)

    #n9.next = n3

    result = isLoopInList(h)

    print(result)

if __name__ == "__main__":
    main()