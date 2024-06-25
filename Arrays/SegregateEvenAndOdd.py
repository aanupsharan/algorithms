def segregate_even_and_odd(arr):
    left, right = 0, len(arr) - 1

    while left < right:
        while arr[left] % 2 == 0 and left < right:
            left += 1
        
        while arr[right] % 2 == 1 and left < right:
            right -= 1
        
        if left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr 
if __name__ == "__main__":
    arr = [12, 34, 45, 9, 8, 90, 3]
    arr = segregate_even_and_odd(arr)

    for i in range(len(arr)):
        print(arr[i], end=" ")