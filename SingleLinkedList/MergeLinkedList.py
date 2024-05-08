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
    
    def pushEnd(self, tail, data):
        new_node = Node(data)
        if tail != None:
            tail.next = new_node
            tail = tail.next
        else:
            self.head = new_node
            tail = self.head
        return tail

def merge(head1, head2):
    if head1 == None and head2 == None:
        return None

    merge_list = SingleLinkedList()
    tail = None
    
    while True:
        if head1 is None:
            tail.next = head2
            break
        if head2 is None:
            tail.next = head1
            break

        if head1.data > head2.data:
            tail = merge_list.pushEnd(tail, head2.data)
            head2 = head2.next
        else:
            tail = merge_list.pushEnd(tail, head1.data)
            head1 = head1.next
   
    return merge_list
if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.push(10)
    l1.push(8)
    l1.push(6)
    l1.push(4)
    l1.push(2)

    l1.printList()

    l2 = SingleLinkedList()
    l2.push(11)
    l2.push(9)
    l2.push(7)
    l2.push(5)
    l2.push(3)
    l2.push(1)

    l2.printList()

    merge_list = merge(l1.head, l2.head)

    merge_list.printList()