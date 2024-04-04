from TreeNode import TreeNode

def isBSTMorrisAlgorithm(root):
    if root == None:
        return False
    if root.left == None or root.right == None:
        return True
    
    curr = root
    prev = None

    while curr != None:
        if curr.left is None:
            if prev != None and prev.value >= curr.value:
                return False
            prev = curr
            curr = curr.right
        else:
            pred = curr.left
            while pred.right != None and pred.right != curr:
                pred = pred.right
            if pred.right is None:
                pred.right = curr
                curr = curr.left
            else:
                if prev != None and prev.value >= curr.value:
                    return False
                prev = curr
                pred.right = None
                curr = curr.right
    return True

if __name__ == "__main__":
    root1 = TreeNode(4)
    root1.left = TreeNode(2)
    root1.right = TreeNode(5)
    root1.left.left = TreeNode(1)
    root1.left.right = TreeNode(3)

    if isBSTMorrisAlgorithm(root1):
        print("It is BST")
    else:
        print("It is not BST")
