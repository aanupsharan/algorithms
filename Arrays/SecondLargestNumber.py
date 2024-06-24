def second_largest_element(arr):
    arr_size = len(arr)

    if arr_size < 2:
        print("invalid inputs")
    
    first = second = float("-inf")

    for i in range(arr_size):
        if arr[i] > first:
            second = first
            first = arr[i]
        if arr[i] > second and arr[i] != first:
            second = arr[i]
    return second

if __name__ == "__main__":
    arr1 = [6, 8, 1, 9, 2, 1, 10, 10]
    second_largest = second_largest_element(arr1)
    print(second_largest)