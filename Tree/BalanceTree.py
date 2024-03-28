import sys
sys.path.append('../')

from TreeNode import TreeNode

def isBalanced(root):
    if root is None:
        return True, 0
    left = isBalanced(root.left)
    right = isBalanced(root.right)

    lhsans = left[0]
    rhsans = right[0]

    diff = abs(left[1] - right[1]) <= 1
    height = max(left[1],right[1]) + 1
    
    if lhsans and rhsans and diff:
        return True, height
    else:
        return False, height
    

def isBalancedTree(root):
    return isBalanced(root)[0]


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    if isBalancedTree(root) :
        print("Tree is Balanced")
    else:
        print("Tree is not Balanced")