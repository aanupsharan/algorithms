def missing_elements(arr, n, low, high):
    s = set(arr)

    for x in range(low, high+1, 1):
        if x not in s:
            print(x, end=" ") 



if __name__ == "__main__":
    arr = [1, 3, 5, 4]
    n = len(arr)
    low, high = 1, 10
    missing_elements(arr, n, low, high)