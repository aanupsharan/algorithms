import sys
sys.path.append('../')

from TreeNode import TreeNode
from BinaryTree import BinaryTree

def inorder(root):
    if root == None:
        return

    current = root
    while current != None:
        if current.left == None:
            print(current.value, end=" ")
            current = current.right
        else:
            predecessor = current.left
            while predecessor.right != current and predecessor.right != None:
                predecessor = predecessor.right

            if predecessor.right == None:
                predecessor.right = current
                current = current.left
            else:
                predecessor.right = None
                print(current.value, end=" ")
                current = current.right

if __name__ == "__main__":
    b = BinaryTree()

    r = TreeNode(50)
    r = b.insert(r, 30)
    r = b.insert(r, 20)
    r = b.insert(r, 40)
    r = b.insert(r, 70)
    r = b.insert(r, 60)
    r = b.insert(r, 80)

    inorder(r)
