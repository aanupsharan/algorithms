import sys
sys.path.append('../')

from TreeNode import TreeNode
from BinaryTree import BinaryTree

def daimeter(root):
    dmeter = 0
    curr = root

    while curr != None:
        if curr.left == None:
            curr = curr.right
        else:
            pre = curr.left
            while pre.right != None and pre.right != curr:
                pre = pre.right
            if pre.right == None:
                pre.right = curr
                curr = curr.left
            else:
                pre.right = None
                lHeight = 0
                rHeight = 0
                temp = curr.left
                while temp != None:
                    lHeight += 1
                    temp = temp.right
                temp = curr.right
                while temp != None:
                    rHeight += 1
                    temp = temp.left
                dmeter = max(dmeter, lHeight + rHeight + 1)
                curr = curr.right
    return dmeter


if __name__ == "__main__":

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)


    cnt = daimeter(root)
    print("daimeter is "+ str(cnt))