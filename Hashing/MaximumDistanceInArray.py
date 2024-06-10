def max_distance(arr):
    mp = {}
    max_dist = 0
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = i
        else:
            max_dist = max(max_dist, i-mp[arr[i]])
    return max_dist

if __name__=='__main__': 
    arr = [3, 2, 1, 2, 1, 4, 5, 8, 6, 7, 4, 2] 
    n = len(arr) 
    print (max_distance(arr)) 