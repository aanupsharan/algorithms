from TreeNode import TreeNode

def isIdentical(root1, root2):
    if root1 == None and root2 == None:
        return True
    if root1 == None or root2 == None:
        return False
    
    return root1.value == root2.value and isIdentical(root1.left, root2.left) and isIdentical(root1.right, root2.right)

def isSubTree(T, S):

    if T == None and S == None:
        return True
    if T == None or S == None:
        return False

    if isIdentical(T, S):
        return True

    return isSubTree(T.left, S) or isSubTree(T.right, S)
    
if __name__ == "__main__":
    T = TreeNode(26)
    T.right = TreeNode(3)
    T.right.right = TreeNode(3)
    T.left = TreeNode(10)
    T.left.left = TreeNode(4)
    T.left.left.right = TreeNode(30)
    T.left.right = TreeNode(6)

    S = TreeNode(10)
    S.right = TreeNode(6)
    S.left = TreeNode(4)
    S.left.right = TreeNode(30)

    if isSubTree(T, S):
        print("Tree 2 is subtree of Tree 1")
    else:
        print("Tree 2 is not a subtree of Tree 1")