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

def intersectionList(head1, head2):
    if head1 == None or head2 == None:
        return None
    
    intersection_list = SingleLinkedList()
    curr1, curr2 = head1, head2
    tail = None

    while curr1 != None and curr2 != None:
        if curr1.data == curr2.data:
            tail = intersection_list.pushEnd(tail, curr1.data)
            curr1 = curr1.next
            curr2 = curr2.next
        elif curr1.data < curr2.data:
            curr1 = curr1.next
        else:
            curr2 = curr2.next
    
    return intersection_list

if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.push(6)
    l1.push(4)
    l1.push(3)
    l1.push(2)
    l1.push(1)

    l2 = SingleLinkedList()
    l2.push(6)
    l2.push(4)
    l2.push(2)

    l3 = intersectionList(l1.head, l2.head)

    l3.printList()
