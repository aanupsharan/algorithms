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

    def remove(self, k):
        if self.head == None:
            return
        
        if k == 1:
            self.head = None
            return
        
        prev, curr, cnt = None, self.head, 0

        while curr != None:
            cnt += 1
            if cnt == k:
                prev.next = curr.next
                curr.next = None
                cnt = 0

            if cnt != 0:
                prev = curr
            curr = prev.next

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
    l.remove(3)
    l.printList()
