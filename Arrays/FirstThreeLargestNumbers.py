def firstThreeLargestNumbers(arr):
    arr_size = len(arr)

    if arr_size < 3:
        print("invalid inputs")
        
    first = second = third = float("-inf")

    for i in range(arr_size):
        if arr[i] > first:
            third = second
            second = first
            first = arr[i]

        if arr[i] > second and arr[i] != first:
            third = second
            second = arr[i]

        if arr[i] > third and arr[i] != second and arr[i] != first:
            third = arr[i]

    print("Three largest elements are", first, second, third)

if __name__ == "__main__":
    arr1 = [6, 8, 1, 9, 2, 1, 10, 10]
    firstThreeLargestNumbers(arr1)