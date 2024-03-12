from TreeNode import TreeNode

class BinaryTree:
    def insert(self, root, data):
        if root == None:
            return TreeNode(data)
        else: 
            if root == data:
                return root
            elif root.value > data:
                root.left = self.insert(root.left, data)
            else:
                root.right = self.insert(root.right, data)
        return root

    def inorder(self, root):
        if root != None:
            self.inorder(root.left)
            print(root.value, end=" ")
            self.inorder(root.right)

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

