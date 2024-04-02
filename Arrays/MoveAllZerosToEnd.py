def moveAllZerosToEnd(arr):
    arr_size = len(arr)

    count = 0
    for i in range(arr_size):
        print("i :: "+str(i))
        if arr[i] != 0:
            arr[count] = arr[i]
            count += 1
    while count < arr_size:
            arr[count] = 0
            count += 1
    return arr

if __name__ == "__main__":
    arr1 = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0, 9] 
    arr1 = moveAllZerosToEnd(arr1)
    print(arr1)