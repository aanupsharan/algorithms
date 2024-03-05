from Node import Node

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def printList(self):
        if self.head == None:
            print("Empty Linked list")
        temp = self.head
        while temp != None:
            print(temp.val)
            if temp.next != None:
                print("|")
            temp = temp.next
        print("=====================")


    
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
    
    def deleteNodeFromEnd(self):
        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
        else:
            temp = self.head
            while temp.next.next != None :
                temp = temp.next
            temp.next = None
    
    def deleteNodeFromStart(self):
        if self.head == None:
            return
        elif self.head.next == None:
            self.head = None
        else:
            self.head = self.head.next

    def deleteNodeByValue(self, value):
        if self.head == None:
            return
        if self.head.val == value:
            self.head = self.head.next
        else:
            temp1, temp2 = self.head, self.head.next
            while temp2 != None:
                if temp2.val == value:
                    temp1.next = temp2.next
                    temp2.next = None
                    break
                temp1 = temp1.next
                temp2 = temp2.next
            print("The "+ str(value) +" is not found in the list")

    def lengthOfList(self):
        if self.head == None:
            return 0

        curr = self.head
        count = 0

        while curr != None:
            count += 1
            curr = curr.next

        return count
            

def main():
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

    """
    h.deleteNodeFromEnd()
    h.deleteNodeFromEnd()
    h.deleteNodeFromEnd()
    h.deleteNodeFromEnd()
    h.deleteNodeFromEnd()
    h.deleteNodeFromEnd()
    """

    """
    h.deleteNodeFromStart()
    h.printList()
    h.deleteNodeFromEnd()
    h.printList()
    h.deleteNodeFromStart()
    h.printList()
    h.deleteNodeFromEnd()
    h.printList()
    h.deleteNodeFromStart()
    h.printList()
    """

    h.deleteNodeByValue(0)
    h.printList()




if __name__ == "__main__":
    main()