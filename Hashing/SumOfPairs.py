def print_pairs(arr, n):
    s = set()
    for i in range(len(arr)):
        if n - arr[i] in s:
            return True
        s.add(arr[i])
    return False

if __name__ == "__main__":
    arr = [1, 4, 45, 6, 10, 8]
    n = 16
    print(print_pairs(arr, n))

