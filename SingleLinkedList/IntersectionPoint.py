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
    

def count(head):
    if head == None:
        return 0
    cnt = 0
    curr = head
    while curr != None:
        cnt += 1
        curr = curr.next

    return cnt

def hasIntersection(head1, head2):
    if head1 == None:
        return False, None
    if head2 == None:
        return False, None
    
    node_count_list1 = count(head1)
    node_count_list2 = count(head2)

    curr1 = head1
    curr2 = head2
    if node_count_list1 > node_count_list2:
        cnt = node_count_list1 - node_count_list2
        print(cnt)
        for i in range(0, cnt):
            curr1 = curr1.next
    else:
        cnt = node_count_list2 - node_count_list1
        for i in range(0, cnt):
            curr2 = curr2.next

    while curr1 != None and curr2 != None:
        if curr1 == curr2:
            return True, curr1
        curr1 = curr1.next
        curr2 = curr2.next
    
    return False, None
    

if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.push(30)
    l1.push(15)
    l1.push(9)
    l1.push(6)
    l1.push(3)

    l2 = SingleLinkedList()
    l2.push(10)

    l2.head.next = l1.head.next.next.next

    result, node = hasIntersection(l1.head, l2.head)

    print(result)
    print(node.data)


