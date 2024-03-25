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
def heightIterative(root):
    if root == None:
        return 0
    queue = []
    queue.append(root)
    queue.append(None)
    height = 0
    while len(queue) > 0:
        temp = queue.pop(0)
        if temp == None :
            height += 1
        if temp != None:
            if temp.left != None:
                queue.append(temp.left)
            if temp.right != None:
                queue.append(temp.right)
        elif len(queue) > 0:
            queue.append(None)
    return height
            
        

if __name__ == "__main__":
    b = BinaryTree()

    r = TreeNode(50)
    r = b.insert(r, 30)
    r = b.insert(r, 20)
    r = b.insert(r, 40)
    r = b.insert(r, 70)
    r = b.insert(r, 60)
    r = b.insert(r, 80)

    count = heightIterative(r)
    print("The height of the Tree:"+str(count))