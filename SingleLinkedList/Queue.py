from Node import Node

class Queue:
    
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        if self.front == None:
            return True
        return False

    def enqueue(self, item):
        if(self.rear == None):
            self.front = self.rear = Node(item)
            return
        self.rear.next = Node(item)
        self.rear = self.rear.next
    
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        temp = self.front
        self.front = self.front.next
        temp.next = None

        if self.front == None:
            self.rear = None

if __name__ == '__main__':
    q = Queue()
    q.enqueue(10)
    q.enqueue(20)
    q.dequeue()
    q.dequeue()
    q.enqueue(30)
    q.enqueue(40)
    q.enqueue(50)
    q.dequeue()
    print("Queue Front : " + str(q.front.val if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.val if q.rear != None else -1))