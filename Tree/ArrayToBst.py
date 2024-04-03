from TreeNode import TreeNode

def convertArrayToBST(arr):
    if not arr:
        return None
    
    mid = len(arr) // 2

    root = TreeNode(arr[mid])

    root.left = convertArrayToBST(arr[:mid])
    root.right = convertArrayToBST(arr[mid+1:])

    return root
     

def preorder(root):
    if root is None:
        return
    
    print(root.value, end=" ")
    preorder(root.left)
    preorder(root.right)

if __name__ == "__main__":
    arr = [1,2,3,4,5,6,7,8]
    root = convertArrayToBST(arr)
    preorder(root)