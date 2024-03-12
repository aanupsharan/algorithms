from TreeNode import TreeNode
from BinaryTree import BinaryTree

def height(root):
    if root == None:
        return 0
    else:
        lHeight = height(root.left)
        rHeight = height(root.right)

        if lHeight > rHeight:
            return lHeight + 1
        else:
            return rHeight + 1

if __name__ == "__main__":
    b = BinaryTree()

    r = TreeNode(50)
    r = b.insert(r, 30)
    r = b.insert(r, 20)
    r = b.insert(r, 40)
    r = b.insert(r, 70)
    r = b.insert(r, 60)
    r = b.insert(r, 80)

    count = height(r)
    print("The height of the Tree:"+str(count))