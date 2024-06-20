def length_longest_subarray(arr):
    
    mp = {}
    sum = 0
    max_length = 0
    
    for i in range(len(arr)):
        sum += arr[i]
        
        if sum == 0:
            max_length = i+1
        
        if sum in mp.keys():
            max_length = max(max_length, i - mp[sum])
        else:
            mp[sum] = i
    return max_length
    
if __name__ == "__main__":
    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    print(length_longest_subarray(arr))