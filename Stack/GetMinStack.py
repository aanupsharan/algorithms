class Stack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, data):
        if self.is_empty():
            self.min_stack.insert(0, data)
        else:
            min_value = self.get_min()
            if data < min_value:
                self.min_stack.insert(0, data)
        self.stack.insert(0, data)
    
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return None
        
        val = self.stack.pop(0)
        if val == self.min_stack[0] or self.top() < self.get_min():
            self.min_stack.pop(0)
        return val
    
    def top(self):
        if self.is_empty():
            return None
        return self.stack[0]

    def get_min(self):
        if self.is_empty():
            return None
        return self.min_stack[0]

    def is_empty(self):
        return len(self.stack) == 0

if __name__ == "__main__":
    s = Stack()
    s.push(5)
    s.push(4)
    s.push(6)
    s.push(3)


    s.pop()
    s.pop()
    s.pop() 
    
    print(s.stack)
    print(s.min_stack)