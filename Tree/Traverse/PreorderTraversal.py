import sys
sys.path.append('../')

from TreeNode import TreeNode

def preorder(root):
    if root == None:
        return
    if root.left == None and root.right == None:
        print(root.value, end=" ")
    
    stack = []
    stack.append(root)
    
    while len(stack) > 0:
        curr = stack.pop(0)
        print(curr.value, end=" ")

        if curr.right != None:
            stack.insert(0, curr.right)
        if curr.left != None:
            stack.insert(0, curr.left)

if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)

    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    preorder(root)