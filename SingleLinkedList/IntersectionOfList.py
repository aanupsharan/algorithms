from SingleLinkedList import SingleLinkedList
from Node import Node

def intersectionNodeOfList(list1, list2):
    if list1.head == None or list2.head == None:
        return None
    
    ptr1 = list1.head
    ptr2 = list2.head

    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

        if ptr1 == ptr2:
            return ptr1
        if ptr1 == None:
            ptr1 = list2.head
        if ptr2 == None:
            ptr2 = list1.head

    return ptr1

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
    hh = SingleLinkedList()



    h.insertNodeAtEnd(n1)
    hh.insertNodeAtEnd(n2)
    h.insertNodeAtEnd(n3)
    hh.insertNodeAtEnd(n4)
    h.insertNodeAtEnd(n5)
    hh.insertNodeAtEnd(n6)
    h.insertNodeAtEnd(n7)
    hh.insertNodeAtEnd(n8)
    h.insertNodeAtEnd(n9)

    result = intersectionNodeOfList(h, hh)

    if result != None:
        print(result.val)
    else:
        print("No intersection Node")

if __name__ == "__main__":
    main()