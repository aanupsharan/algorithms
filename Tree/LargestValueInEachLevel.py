from TreeNode import TreeNode

def largestValues(root):
    if root is None:
        return []
    
    result = []
    if root.left is None and root.right is None:
        result.append(root.value)
        return 

    queue = []
    queue.append(root)
    queue.append(None)
    maxValue = float('-inf')
    
    while len(queue) > 0:
        curr = queue.pop(0)
        
        if curr == None:
            result.append(maxValue)
            maxValue = float('-inf')
        if curr != None:
            maxValue = max(maxValue, curr.value)
            if curr.left != None:
                queue.append(curr.left)
            if curr.right != None:
                queue.append(curr.right)
        elif len(queue) > 0:
            queue.append(None)

    return result
            
        

if __name__ == "__main__":
    root1 = TreeNode(4)
    root1.left = TreeNode(9)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(5)
    root1.right.right = TreeNode(7)

    result = largestValues(root1)

    print(result)