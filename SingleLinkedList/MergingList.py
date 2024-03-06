from SingleLinkedList import SingleLinkedList
from Node import Node

def mergeList(l, ll):
    if l.head == None and ll.head == None:
        return
    elif l.head == None:
        return ll
    elif ll.head == None:
        return l

    l_curr, ll_curr = l.head, ll.head
    l_next, ll_next = None, None

    while l_curr != None and ll_curr != None:
        l_next = l_curr.next
        ll_next = ll_curr.next

        l_curr.next = ll_curr
        ll_curr.next = l_next

        l_curr = l_next
        ll_curr = ll_next
    
    ll.head = ll_curr
    return l, ll
    


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



    #h.insertNodeAtEnd(n1)
    hh.insertNodeAtEnd(n2)
    #h.insertNodeAtEnd(n3)
    hh.insertNodeAtEnd(n4)
    #h.insertNodeAtEnd(n5)
    hh.insertNodeAtEnd(n6)
    h.insertNodeAtEnd(n7)
    hh.insertNodeAtEnd(n8)
    h.insertNodeAtEnd(n9)

    q, qq = mergeList(h, hh)

    q.printList()
    if qq != None:
        qq.printList()

if __name__ == "__main__":
    main()