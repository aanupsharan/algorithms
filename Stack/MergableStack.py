class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if self.head == None:
            return True
        return False

    def pop(self):
        if isEmpty():
            print("Stack Under flow")
        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None

    def push(self, data):
        new_node = Node(data)

        if self.head != None:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        else:
            self.head = new_node
            self.head.next = None
            self.head.prev = None
            self.tail = new_node
    
    def merge(self, stack):
        if stack.head == None:
            return
        if self.isEmpty():
            self.head = stack.head
            self.tail = stack.tail
        else:
            self.tail.next = stack.head
            self.tail = stack.tail

    def display(self):
        if self.isEmpty():
            print("Stack is empty")
        else:
            temp = self.head

            while temp != self.tail:
                print(temp.data, end="->")
                temp = temp.next
            print(temp.data)
if __name__ == "__main__":
    ms1 = Stack()
    ms2 = Stack()
 
    ms1.push(6) 
    ms1.push(5)
    ms1.push(4)
    ms2.push(9)
    ms2.push(8)
    ms2.push(7)
    ms1.display()
    ms2.display()
    ms1.merge(ms2)
    ms1.display()