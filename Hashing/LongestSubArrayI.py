def longest_length_sub_array(arr, k):
    
    mp = {}
    sum = 0
    max_length = 0

    for i in range(len(arr)):
        sum += arr[i]
        mod = sum % k

        if mod < 0:
            mod += k
        
        if mod == 0:
            max_length = i+1
        elif mod in mp.keys():
            if (max_length < (i - mp[mod])):
                max_length = i - mp[mod]
            else:
                mp[mod] = i
    return max_length

if __name__ == "__main__":
    arr = [4,5,0,-2,-3,1]
    k = 5

    print(longest_length_sub_array(arr, k))