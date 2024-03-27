import sys
sys.path.append('../')

from TreeNode import TreeNode
from BinaryTree import BinaryTree

def MirrorTree(root):
    if not root or (not root.left and not root.right):
        return
    queue = []
    queue.append(root)

    while len(queue) > 0:
        curr = queue.pop(0)
        curr.left, curr.right = curr.right, curr.left

        if curr.left:
            queue.append(curr.left)
        if curr.right:
            queue.append(curr.right)


if __name__ == "__main__":
    b = BinaryTree()

    r = TreeNode(50)
    r = b.insert(r, 30)
    r = b.insert(r, 20)
    r = b.insert(r, 40)
    r = b.insert(r, 70)
    r = b.insert(r, 60)
    r = b.insert(r, 80)

    b.inorder(r)

    MirrorTree(r)

    b.inorder(r)


