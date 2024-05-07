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
    
    def isPalindrome(self):
        if self.head == None:
            return False
        stack = []

        curr = self.head
        while curr != None:
            stack.insert(0, curr.data)
            curr = curr.next

        curr = self.head
        while curr != None:
            s = stack.pop(0)
            if curr.data != s:
                return False
            curr = curr.next
        
        return True
if __name__ == "__main__":
    l1 = SingleLinkedList()
    l1.push(1)
    l1.push(2)
    l1.push(3)
    l1.push(2)
    l1.push(4)

    if l1.isPalindrome():
        print("The element is palindrome")
    else:
        print("The element is not palindrome")