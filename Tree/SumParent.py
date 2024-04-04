from TreeNode import TreeNode

def isSumParentNode(root):
    if root == None or (root.left == None and root.right == None):
        return True
    
    queue = []
    queue.append(root)
    queue.append(None)

    while len(queue):
        curr = queue.pop(0)

        if curr == None:
            if len(queue) > 0:
                queue.append(None)
            continue
        sum = 0
        if curr.left != None:
            queue.append(curr.left)
            sum += curr.left.value
        if curr.right != None:
            queue.append(curr.right)
            sum += curr.right.value

        if curr.value != sum and sum != 0:
            return False
    return True

if __name__ == "__main__":
    root1 = TreeNode(10)
    root1.left = TreeNode(8)
    root1.right = TreeNode(2)
    root1.left.left = TreeNode(3)
    root1.left.right = TreeNode(5)

    print(isSumParentNode(root1))