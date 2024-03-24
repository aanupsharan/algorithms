import sys
sys.path.append('../')

from TreeNode import TreeNode
from BinaryTree import BinaryTree

def levelOrderTraversal(root):
    if root == None:
        return
    queue = []
    temp = root
    queue.append(temp)

    while len(queue) > 0:
        temp = queue.pop(0)
        print(temp.value, end = " ")
        if temp.left != None:
            queue.append(temp.left)
        if temp.right != None:
            queue.append(temp.right)
    

if __name__ == "__main__":
    b = BinaryTree()

    r = TreeNode(50)
    r = b.insert(r, 30)
    r = b.insert(r, 20)
    r = b.insert(r, 40)
    r = b.insert(r, 70)
    r = b.insert(r, 60)
    r = b.insert(r, 80)

    levelOrderTraversal(r)