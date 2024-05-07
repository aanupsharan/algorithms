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

def multiply(head1, head2):
    if head1 == None or head2 == None:
        return 0
    
    first = head1
    second = head2
    num1 = 0
    num2 = 0

    while first != None:
        num1 = num1 * 10 + first.data
        first = first.next
    
    while second != None:
        num2 = num2 * 10 + second.data
        second = second.next
    
    multiply = num1 * num2

    return multiply

if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.push(6)
    l1.push(4)
    l1.push(9)
    l1.push(5)
    l1.push(7)

    l2 = SingleLinkedList()
    l2.push(4)
    l2.push(8)

    result = multiply(l1.head, l2.head)
    print(result)
    