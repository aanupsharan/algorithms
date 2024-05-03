class Node:
    def __init__(self, x):
        self.data = x
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def printList(self): 
        temp = self.head 
        while temp is not None: 
            print(temp.data, end='->') 
            temp = temp.next
        print("NULL\n")

    def removeLoop(self, loop_node):
        ptr1 = loop_node
        ptr2 = loop_node
        
        
        k = 1 
        while(ptr1.next != ptr2):
            ptr1 = ptr1.next
            k += 1


        ptr1 = self.head        
        ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next

        
        while(ptr2 != ptr1):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        # Get pointer to the last node
        while(ptr2.next != ptr1):
            ptr2 = ptr2.next

        
        ptr2.next = None

    def detectLoop(self):
        if self.head == None:
            return
        slow = self.head
        fast = self.head

        #Detect the loop.
        while slow != None and fast != None:
            if slow is fast:
                self.removeLoop(fast)
                return
            slow = slow.next
            fast = fast.next.next

if __name__ == "__main__":
    llist = LinkedList()
    llist.head = Node(50)
    llist.head.next = Node(20)
    llist.head.next.next = Node(15)
    llist.head.next.next.next = Node(4)
    llist.head.next.next.next.next = Node(10)

    # Create a loop for testing
    llist.head.next.next.next.next.next = llist.head.next.next

    llist.detectLoop()
    llist.printList()
