class Stack:
    def __init__(self):
        self.stack = []
        self.top = -1
    
    def push(self,data):
        self.top += 1
        self.stack.insert(self.top, data)
    
    def pop(self):
        if not self.isEmpty():
            s = self.stack.pop(self.top)
            self.top -= 1
            return s

    def peek(self):
        if not self.isEmpty():
            return self.stack[self.top]
        return int('inf')
    
    def isEmpty(self):
        return self.top == -1 

class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
      self.queue.append(data)

    def dequeue(self):
        q = self.queue.pop(0)
        return q

    def isEmpty(self):
        return len(self.queue) == 0
    
    def length(self):
        return len(self.queue)

    def getRear(self):
        if not self.isEmpty():
            return self.queue[-1]
        return int('-inf')

def isSortable(q1, q2, s):
    if q1.isEmpty():
        return False 

    lengthOfQ1 = q1.length()
    while not q1.isEmpty():
        temp = q1.dequeue()
        
        if s.isEmpty():
            s.push(temp)
            continue

        if temp < s.peek():
            q2.enqueue(temp)
        else:
            s.push(temp)
    
    while not s.isEmpty() and s.peek() > q2.getRear():
        q2.enqueue(s.pop())
    
    if lengthOfQ1 == q2.length() and s.isEmpty():
        return True
    return False
        


    
if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()
    s = Stack()

    q1.enqueue(6)
    q1.enqueue(7)
    q1.enqueue(2)
    q1.enqueue(3)
    q1.enqueue(4)

    result = isSortable(q1, q2, s)
    print(result)




    
