def next_greater_frequency(a, n):
    if n == 0:
        return None

    stack = []
    ans = n * [-1]

    frequency = dict()

    for i in range(0, n):
        try:
            frequency[a[i]] += 1
        except:
            frequency[a[i]] = 1
    
    for i in range(n-1, -1, -1):
        
        while len(stack) > 0 and frequency[a[i]] >= frequency[stack[0]]:
            stack.pop(0)
        
        if len(stack) > 0:
            ans[i] = stack[0]
        
        stack.insert(0, a[i])
    
    return ans


if __name__ == "__main__":
    #a = [1, 1, 2, 3, 4, 2, 1]
    a = [1, 1, 1, 2, 2, 2, 2, 11, 3, 3]
    print(next_greater_frequency(a, len(a)))