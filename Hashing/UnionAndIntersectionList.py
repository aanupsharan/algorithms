class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def push(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.next = self.head
            self.head = new_node

    def append(self, data):
        new_node = Node(data)
        if self.tail == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = self.tail.next
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
    
    def get_intersection(self, head1, head2):
        if head1 == None or head2 == None:
            return None

        curr1 = head1
        hset = set()
        result = LinkedList()

        while curr1 != None:
            hset.add(curr1.data)
            curr1 = curr1.next

        curr2 = head2
        while curr2 != None:
            if curr2.data in hset:
                result.append(curr2.data)
            curr2 = curr2.next
        
        return result
    
    def get_union(self, head1, head2):
        if head1 == None or head2 == None:
            return None

        result = LinkedList()
        hset = set()

        curr = head1
        while curr != None:
            hset.add(curr.data)
            curr = curr.next
        
        curr = head2
        while curr != None:
            hset.add(curr.data)
            curr = curr.next
        
        for val in hset:
            result.append(val)

        return result
        
if __name__ == "__main__":
    llist1 = LinkedList()
    llist2 = LinkedList()
    intersection = LinkedList()
    union_list = LinkedList()
 
    # create a linked list 10->15->4->20
    llist1.push(20)
    llist1.push(4)
    llist1.push(15)
    llist1.push(10)
 
    # create a linked list 8->4->2->10 
    llist2.push(10)
    llist2.push(2)
    llist2.push(4)
    llist2.push(8)
 
    intersection = intersection.get_intersection(
               llist1.head, llist2.head)
    union_list = union_list.get_union(
             llist1.head, llist2.head)
 
    print("First List is")
    llist1.print_list()
 
    print("Second List is")
    llist2.print_list()
 
    print("Intersection List is")
    intersection.print_list()
 
    print("Union List is")
    union_list.print_list()


        