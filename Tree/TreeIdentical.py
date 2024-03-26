import sys
sys.path.append('../')

from TreeNode import TreeNode

def isIdenticalByLevelOrder(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    
    q1 = []
    q2 = []
    q1.append(r1)
    q2.append(r2)

    while len(q1) > 0 and len(q2) > 0:
        curr1 = q1.pop(0)
        curr2 = q2.pop(0)

        if curr1.value != curr2.value:
            return False

        if curr1.left:
            q1.append(curr1.left)
        if curr1.right:
            q1.append(curr1.right)
        if curr2.left:
            q2.append(curr2.left)
        if curr2.right:
            q2.append(curr2.right)

    return not len(q1) > 0 and not len(q2) > 0

def isIdentical(r1, r2):
    if not r1 and not r2:
        return True
    if not r1 or not r2:
        return False
    
    #Morris Traversal
    while r1 and r2:
        if r1.value != r2.value:
            return False
        
        if not r1.left:
            r1 = r1.right
        else:
            pred = r1.left
            while pred.right and pred.right != r1:
                pred = pred.right
            if not pred.right:
                pred.right = r1
                r1 = r1.left
            else:
                pred.right = None
                r1 = r1.right
        
        if not r2.left:
            r2 = r2.right
        else:
            pred = r2.left
            while pred.right and pred.right != r2:
                pred = pred.right
            if not pred.right:
                pred.right = r2
                r2 = r2.left
            else:
                pred.right = None
                r2 = r2.right
    return (not r1) and (not r2)

if __name__ == "__main__":
    # Construct the first tree
    root1 = TreeNode(1)
    root1.left = TreeNode(2)
    root1.right = TreeNode(3)
    root1.left.left = TreeNode(4)
    root1.left.right = TreeNode(5)
 
    # Construct the second tree
    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(3)
    root2.left.left = TreeNode(4)
    root2.left.right = TreeNode(5)

    if isIdenticalByLevelOrder(root1, root2):
        print("Trees are identical")
    else:
        print("Trees are not identical")

