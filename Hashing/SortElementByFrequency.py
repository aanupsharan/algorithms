from collections import defaultdict

def sort_by_frequency(arr, n):
    d = defaultdict(lambda: 0)

    for i in range(n):
        if arr[i] in d:
            d[arr[i]] += 1
        else:
            d[arr[i]] = 1 
    arr.sort(key = lambda x: (-d[x],x))
    print(arr)

if __name__ == "__main__":
    arr = [2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8]
    n = len(arr)
    
    solution = sort_by_frequency(arr, n)
    print(solution)