import sys
sys.path.append('../')

from TreeNode import TreeNode

def reverseMorrisTraversal(root):
    curr = root

    while curr != None:
        if curr.right == None:
            print(curr.value, end=" ")
            curr = curr.left
        else:
            succ = curr.right
            while succ.left != None and succ.left != curr:
                succ = succ.left
            if succ.left == None:
                succ.left = curr
                curr = curr.right
            else:
                succ.left = None
                print(curr.value, end=" ")
                curr = curr.left


if __name__ == "__main__":
    root = TreeNode(20)
    root.left = TreeNode(8)
    root.right = TreeNode(22)

    root.left.left = TreeNode(4)
    root.left.right = TreeNode(12)

    root.left.right.left = TreeNode(10)
    root.left.right.right = TreeNode(14)

    reverseMorrisTraversal(root)