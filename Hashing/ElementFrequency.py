def most_frequent(arr):
    frequency = dict()
    for i in range(len(arr)):
        if arr[i] in frequency.keys():
            frequency[arr[i]] += 1
        else:
            frequency[arr[i]] = 1
    
    max_count = 0
    res = -1
    for i in frequency:
        if max_count < frequency[i]:
            res = i
            max_count = frequency[i]
    return res

if __name__ == "__main__":
    arr = [40,50,30,40,50,30,30] 

    print(most_frequent(arr)) 
