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
    
    def deleteNodeWithoutHead(self, pos):
        if pos is None:
            return
        elif pos.next is None:
            print("This is last node, require head, can't be freed\n") 
            return
        
        pos.data = pos.next.data
        pos.next = pos.next.next

if __name__ == "__main__":
    l = SingleLinkedList()
    l.push(50)
    l.push(40)
    l.push(30)
    l.push(20)
    l.push(10)

    pos = l.head.next.next.next.next
    print(pos.data)
    l.printList()
    l.deleteNodeWithoutHead(pos)

    l.printList()