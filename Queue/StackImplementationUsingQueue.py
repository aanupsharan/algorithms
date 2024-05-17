class Queue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.is_empty():
            return
        return self.queue.pop(0)
    
class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()
    
    def push(self, data):
        self.q1.enqueue(data)
    
    def pop(self):
        if self.q1.is_empty():
            print("Stack is empty")
        
        while len(self.q1.queue) != 1:
            self.q2.enqueue(self.q1.dequeue())
        
        b = self.q1.dequeue()
        self.q1, self.q2 = self.q2, self.q1
        return b
        

if __name__ == "__main__":
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)
    s.push(5)

    print(s.q1.queue)
    b = s.pop()

    print("b :: ", b)