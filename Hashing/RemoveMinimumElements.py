def minimum_remove(arr1, arr2):
    mp = {}
    for i in range(len(arr1)):
        if arr1[i] not in mp:
            mp[arr1[i]] = 1
        else:
            mp[arr1[i]] += 1
    
    for i in range(len(arr2)):
        if arr2[i] not in mp:
            mp[arr2[i]] = 1
        else:
            mp[arr2[i]] += 1

    sum = 0
    for i in mp:
        if mp[i] > 1:
            sum += 1

    return sum

if __name__ == "__main__":
    arr1 = [5, 4, 9, 2, 3] 
    arr2 = [2, 8, 7, 6, 3]

    print(minimum_remove(arr1, arr2))