def reverse(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end += -1

def left_rotate(arr, d, arr_length):
    if d == 0:
        return
    
    d = d % arr_length

    reverse(arr, 0, d-1)
    reverse(arr, d, arr_length-1)
    reverse(arr, 0, arr_length-1)

def print_array(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    d = 2
    arr_length = len(arr)

    print_array(arr)
    print()
    left_rotate(arr, d, arr_length)
    print_array(arr)