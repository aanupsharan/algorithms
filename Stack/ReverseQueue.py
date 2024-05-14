class Queue:
    def __init__(self):
        self.queue = []
    
    def isEmpty(self):
        return len(self.queue) == 0
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return None
        element = self.queue.pop(0)
        return element

    def printQueue(self):
        print(self.queue)

class Stack:
    def __init__(self):
        self.stack = []
    
    def isEmpty(self):
        return len(self.stack) == 0
    
    def push(self, data):
        self.stack.insert(0, data)
    
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return None
        element = self.stack.pop(0)
        return element

def reverse(queue):
    if queue.isEmpty():
        return
    
    stack = Stack()
    
    while not queue.isEmpty():
        stack.push(queue.dequeue())
    
    while not stack.isEmpty():
        queue.enqueue(stack.pop())

    return queue


if __name__ == "__main__":
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.enqueue(60)
    q.enqueue(70)
    q.enqueue(80)
    q.enqueue(90)
    q.enqueue(100)

    q = reverse(q)

    q.printQueue()



