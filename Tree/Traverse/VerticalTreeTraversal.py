import sys
sys.path.append('../')

from TreeNode import TreeNode

def getVerticalTraversal(root, hd,m):
    if root is None:
        return
    
    try:
        m[hd].append(root.value)
    except:
        m[hd] = [root.value]
    
    getVerticalTraversal(root.left, hd-1, m)
    getVerticalTraversal(root.right, hd+1, m)

def printVerticalTraversal(root):
    if root == None:
        return

    m = dict()
    hd = 0

    getVerticalTraversal(root, hd, m)

    print(str(m))

if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(7)

    root.right.right.left = TreeNode(7)
    root.right.right.right = TreeNode(8)

    printVerticalTraversal(root)