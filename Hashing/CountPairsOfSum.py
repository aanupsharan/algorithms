def get_pairs_count(arr, n, sum):
    frequency = {}
    count = 0
    for i in range(n):
        if sum - arr[i] in frequency:
            count += frequency[sum - arr[i]]
        if arr[i] in frequency:
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1
    
    return count


if __name__ == "__main__":
    arr = [1, 5, 7, -1, 5]
    n = len(arr)
    sum = 6
    print('Count of pairs is', get_pairs_count(arr, n, sum))