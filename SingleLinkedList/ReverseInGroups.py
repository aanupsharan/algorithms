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

    def reverseInGroups(self, head, group_size):
        if head == None:
            return
        prev, next = None, None
        curr = head
        count = 0
        
        while curr != None and count < group_size:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
            count += 1

        if next != None:
            head.next = self.reverseInGroups(next, group_size)
        
        return prev

if __name__ == "__main__":
    l = SingleLinkedList()
    l.push(9)
    l.push(8)
    l.push(7)
    l.push(6)
    l.push(5)
    l.push(4)
    l.push(3)
    l.push(2)
    l.push(1)

    l.printList()

    l.head = l.reverseInGroups(l.head, 3)

    l.printList()