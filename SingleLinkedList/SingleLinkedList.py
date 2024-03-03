class Node:
    def __init__(self, data):
        self.val = data
        self.next = None


class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        temp = self.head
        while temp != None:
            print(temp.val)
            if temp.next != None:
                print("|")
            temp = temp.next


    
    def insertNodeAtEnd(self, node):
        if(node == None):
            return 0;
        if(self.head == None):
            self.head = node;
        else:
            temp = self.head;
            while(temp.next != None):
                temp = temp.next
            temp.next = node
    
    def insertNodeAtStart(self, node):
        node.next = self.head
        self.head = node
                

n1 = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)


h = SingleLinkedList()

"""
h.insertNodeAtEnd(n1)
h.insertNodeAtEnd(n2)
h.insertNodeAtEnd(n3)
h.insertNodeAtEnd(n4)
h.insertNodeAtEnd(n5)
"""


h.insertNodeAtStart(n1)
h.insertNodeAtStart(n2)
h.insertNodeAtStart(n3)
h.insertNodeAtStart(n4)
h.insertNodeAtStart(n5)

h.printList()

