class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None
    
    def isEmpty(self):
        return self.top == None
    
    def push(self, data):
        new_node = Node(data)
        if not self.isEmpty():
            new_node.next = self.top
        self.top = new_node
    
    def pop(self):
        if not self.isEmpty():
            s = self.top
            self.top = self.top.next
            s.next = None
            return s
        return None

    def display(self):
        s = self.top
        while s != None:
            print(s.data,end=" ")
            s = s.next

    def reverse(self):
        if self.isEmpty():
            return
        prev, curr = None, None

        while self.top != None:
            curr = self.top
            self.top = self.top.next
            curr.next = prev
            prev = curr
        
        self.top = curr

if __name__ == "__main__":
    stack = Stack()

    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.push(4)
    stack.push(5)

    stack.display()

    stack.reverse()
    print(" ")
    stack.display()