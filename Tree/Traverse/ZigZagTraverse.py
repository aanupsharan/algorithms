import sys
sys.path.append('../')
from TreeNode import TreeNode

def zigzagTraversal(root):

    if root == None:
        return []
    if root.left == None and root.right == None:
        return [[root.value]]

    queue = []
    level = []
    result = []

    queue.append(root)
    queue.append(None)

    while len(queue) > 0:
        curr = queue.pop(0)
        if curr == None:
            result.append(level)
            level = []
        if curr != None:
            level.append(curr.value)
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

    zigzagResult = zigzagTraversal(root1)

    print(zigzagResult)