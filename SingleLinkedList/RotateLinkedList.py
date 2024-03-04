from SingleLinkedList import SingleLinkedList
from Node import Node

def rotateLinkedList(ll, k):
    if ll.head == None:
        return
    count = 1
    curr = ll.head

    while count < k and curr != None :
        print(curr, count)
        curr = curr.next
        count += 1
    
    if curr == None:
        print("k value is exceeding the number of nodes")
        return

    kthnode = curr

    while curr.next != None:
        curr = curr.next

    curr.next = ll.head
    ll.head = kthnode.next
    kthnode.next = None

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

    rotateLinkedList(h,3)

    h.printList()

if __name__ == "__main__":
    main()