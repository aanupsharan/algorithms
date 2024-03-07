from Node import Node

class Stack:
    
    def __init__(self):
        self.top = None

    def isEmpty(self):
        if self.top != None:
            return False
        return True

    def push(self, item):
        temp = Node(item)
        if self.isEmpty():
            self.top = temp
            return
        temp.next = self.top
        self.top = temp
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        temp = self.top
        self.top = self.top.next
        temp.next = None
        return temp
    
    def peek(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.top.val
    
    def display(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        temp = self.top
        while temp != None:
            print(temp.val)
            temp = temp.next

if __name__ == "__main__":
    MyStack = Stack()
   
    MyStack.push(11)
    MyStack.push(22)
    MyStack.push(33)
    MyStack.push(44)
 
    # Display stack elements
    MyStack.display()
 
    # Print top element of stack
    print("\nTop element is ", MyStack.peek())
 
    # Delete top elements of stack
    MyStack.pop()
    MyStack.pop()
 
    # Display stack elements
    MyStack.display()
 
    # Print top element of stack
    print("\nTop element is ", MyStack.peek())