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

    def reverse(self):
        if self.head == None:
            return
        prev, curr, next = None, self.head, None
        while curr != None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev
        
def add(list1, list2):
    if list1.head == None and list2.head == None:
        return
    if list1.head == None and list2.head != None:
        return list2
    if list1.head != None and list2.head == None:
        return list1

    list1.reverse()
    list2.reverse()

    curr1 = list1.head
    curr2 = list2.head
    carry = 0
    addedList = SingleLinkedList()

    while curr1 != None or curr2 != None or carry == 1:
        new_value = carry
        if curr1 != None:
            new_value += curr1.data
        if curr2 != None:
            new_value += curr2.data
        carry = new_value // 10
        new_value = new_value % 10
        
        addedList.push(new_value)

        if curr1 != None:
            curr1 = curr1.next
        if curr2 != None:
            curr2 = curr2.next

    return addedList

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

    l3 = add(l1, l2)
    l3.printList()

