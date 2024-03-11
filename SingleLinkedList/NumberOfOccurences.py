from SingleLinkedList import SingleLinkedList
from Node import Node

def numberOfOccurenceOfKey(list, key):
    if list.head == None:
        print("key "+str(key)+" appears 0 times")
        return
    count = 0
    curr = list.head

    while curr != None:
        if curr.val == key:
            count += 1
        curr = curr.next
    print("key "+str(key)+" appears "+str(count)+" times")

if __name__ == "__main__":
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(1)
    n4 = Node(2)
    n5 = Node(3)
    n6 = Node(1)
    n7 = Node(1)
    n8 = Node(4)

    h = SingleLinkedList()

    h.insertNodeAtEnd(n1)
    h.insertNodeAtEnd(n2)
    h.insertNodeAtEnd(n3)
    h.insertNodeAtEnd(n4)
    h.insertNodeAtEnd(n5)
    h.insertNodeAtEnd(n6)
    h.insertNodeAtEnd(n7)
    h.insertNodeAtEnd(n8)

    numberOfOccurenceOfKey(h, 1)