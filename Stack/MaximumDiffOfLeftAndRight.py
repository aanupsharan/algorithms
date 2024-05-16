def left_smaller_element(arr, n):
    stack = []
    ans = n * [0]
    for i in range(0, n):
        if len(stack) == 0:
            stack.insert(0,arr[i])
            continue

        while len(stack) != 0 and arr[i] <= stack[0]:
            stack.pop(0)
        
        if len(stack) != 0 and arr[i] > stack[0]:
            ans[i] = stack[0]
        stack.insert(0, arr[i])
    return ans


def right_smaller_element(arr, n):
    stack = []
    ans = n * [0]
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            stack.insert(0,arr[i])
            continue

        while len(stack) != 0 and arr[i] <= stack[0]:
            stack.pop(0)
        
        if len(stack) != 0 and arr[i] > stack[0]:
            ans[i] = stack[0]
        stack.insert(0, arr[i])
    return ans


def maximum_difference(arr):
    n = len(arr)
    left = left_smaller_element(arr, n)
    right = right_smaller_element(arr, n)

    max_diff = 0
    for i in range(0, n):
        max_diff = max(max_diff, abs(left[i] - right[i]))
    
    return max_diff

if __name__ == '__main__':
    arr = [2, 4, 8, 7, 7, 9, 3]
    print("maximum diff :: ", maximum_difference(arr))