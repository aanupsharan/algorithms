class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SingleLinkedList:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def printList(self): 
        temp = self.head 
        while temp is not None: 
            print(temp.data, end='->') 
            temp = temp.next
        print("NULL\n")
    
    def sort(self):
        if self.head == None:
            return

        n0=n1=n2=0
        curr = self.head
        while curr != None:
            if curr.data == 0:
                n0 += 1
            elif curr.data == 1:
                n1 += 1
            else:
                n2 += 1
            curr = curr.next

        ll = SingleLinkedList()
        for cnt in range(0, n2):
            ll.push(2)

        for cnt in range(0, n1):
            ll.push(1)

        for cnt in range(0, n0):
            ll.push(0)

        self.head = ll.head
if __name__ == "__main__":
    l = SingleLinkedList()
    l.push(1)
    l.push(0)
    l.push(2)
    l.push(0)
    l.push(2)
    l.push(1)
    l.push(1)
    l.push(0)
    l.push(1)

    l.printList()
    
    l.sort()

    l.printList()