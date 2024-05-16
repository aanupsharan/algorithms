def is_sortable(arr):
    if arr is None:
        return False
    
    stack = []

    for i in range(0, len(arr)):
        stack.insert(0, arr[i])
    
    while len(stack) != 0:
        b = stack.pop(0)
        if len(stack) != 0 and b > stack[0]:
            return False
    
    return True

if __name__ == '__main__':
    arr = [3,2,1]
    print(is_sortable(arr))