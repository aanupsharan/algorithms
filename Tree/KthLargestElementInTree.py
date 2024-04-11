from TreeNode import TreeNode

def largestValue(tree, k):
    current = root
    count = 0
    while current != None:
        if current.right == None:
            count += 1
            if count == k:
                print("The "+ str(k) +"th largest element is :"+str(current.value))
                return
            current = current.left
        else:
            succesor = current.right
            while succesor.left != None and succesor.left != current:
                succesor = succesor.left
            if succesor.left == None:
                succesor.left = current
                current = current.right
            else:
                succesor.left = None
                count += 1
                if count == k:
                    print("The "+ str(k) +"th largest element is :"+str(current.value))
                    return
                current = current.left
    print("The "+ str(k) +"th largest element is not found")

if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(4)
    root.right = TreeNode(20)

    root.left.left = TreeNode(2)
    
    root.right.left = TreeNode(15)
    root.right.right = TreeNode(40)

    largestValue(root, 4)