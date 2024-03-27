import sys
sys.path.append('../')

from TreeNode import TreeNode
from BinaryTree import BinaryTree

def isSymentricTree(root):
    if not root or (not root.left and not root.right):
        return True

    stack = []
    stack.append(root.left)
    stack.append(root.right)

    while len(stack) > 0:
        node1 = stack.pop()
        node2 = stack.pop()
        
        if not node1 and not node2:
            continue

        if not node1 or not node2:
            return False
        
        if node1.value != node2.value:
            return False

        stack.append(node1.left)
        stack.append(node2.right)
        stack.append(node1.right)
        stack.append(node2.left)

    return True

if __name__ == "__main__":
    b = BinaryTree()

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(3)

    if isSymentricTree(root):
        print("Symentric Tree")
    else:
        print("Not a Symentric Tree")

