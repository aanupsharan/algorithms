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

    def countNodes(self):
        count = 0
        curr = self.head
        while curr != None:
            count += 1
            curr = curr.next
        return count

    def swap(self, k):

        n = self.countNodes()
        
        if n < k:
            return
        
        if 2*k-1 == n:
            return

        x = self.head
        x_prev = None
        for i in range(k - 1):
            x_prev = x
            x = x.next

        y = self.head
        y_prev = None
        for i in range(n-k):
            y_prev = y
            y = y.next
        
        if x_prev != None:
            x_prev.next = y
        
        if y_prev != None:
            y_prev.next = x

        temp = x.next
        x.next = y.next
        y.next = temp

        if k==1:
            self.head = x
        if k == n:
            self.head = y

if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.push(3)
    l1.push(9)
    l1.push(5)
    l1.push(8)
    l1.push(10)
    l1.push(5)

    l1.printList()
    l1.swap(2)
    l1.printList()

