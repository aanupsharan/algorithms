def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def left_array_rotation(arr, k, n):
    
    k = k % n

    reverse(arr, 0, k-1)
    reverse(arr, k, n-1)
    reverse(arr, 0, n-1)
if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    left_array_rotation(arr, k, len(arr))