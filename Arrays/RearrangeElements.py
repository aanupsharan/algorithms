def rearrange(arr):
    size = len(arr);
    if size == 0 or size == 1:
        return arr
    i, k = 0, 0
    j = size - 1
    temp = size * [None]
    while i < j:
        temp[k] = arr[j]
        k += 1
        temp[k] = arr[i]
        k += 1
        i += 1
        j -= 1
    if i == j:
        temp[k] = arr[i]

    return temp

if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    arr = rearrange(arr)
    print(arr)