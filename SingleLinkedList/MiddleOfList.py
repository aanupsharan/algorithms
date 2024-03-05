from SingleLinkedList import SingleLinkedList
from Node import Node



def middleOfSingleLinkedList(ll):
    if ll.head == None:
        return 
    
    len = ll.lengthOfList()
    mid = round(len/2)
    curr = ll.head
   
    while mid != 0:
        curr = curr.next
        mid -= 1
    
    return curr

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

    result = middleOfSingleLinkedList(h)

    print(result.val)

   

if __name__ == "__main__":
    main()