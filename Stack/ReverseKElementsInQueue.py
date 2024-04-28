class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
    
    def dequeue(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        else:
            print("Queue is empty")
    
    def size(self):
        return len(self.queue)
    
    def front(self):
        if size() > 0:
            return self.queue[0]
        else:
            return None
class Stack:
    def __init__(self):
        self.stack = []
    
    def push(self, data):
        self.stack.insert(0, data)
    
    def pop(self):
        if len(self.stack) > 0:
            return self.stack.pop(0)
        else:
            print("Stack is empty")

def reverse(queue, k):
    if queue.size() == None:
        return
    
    if queue.size() < k:
        print("The input's are not correct. K should be less than queue size")
    
    stack = Stack()
    
    for i in range(0, k-1):
        temp = queue.dequeue()
        stack.push(temp)
    
    while len(stack.stack) > 0:
        temp = stack.pop()
        queue.enqueue(temp)

    for i in range(0, queue.size()-k+1):
        temp = queue.dequeue()
        queue.enqueue(temp)



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

    reverse(q, 4)

    print(q.queue)
