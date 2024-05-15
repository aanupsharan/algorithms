def next_smallest_index(hist, n):
    stack = []
    ans = n * [-1]
    
    for i in range(n-1,-1,-1):
        if len(stack) == 0:
            stack.insert(0, i)
            continue
        while len(stack) != 0 and hist[i] <= hist[stack[0]]:
            stack.pop(0)
        
        if len(stack) != 0 and hist[i] > hist[stack[0]]:
            ans[i] = stack[0]
        stack.insert(0, i)


    return ans

def prev_smallest_index(hist, n):
    stack = []
    ans = n * [-1]
    
    for i in range(0,n):
        if len(stack) == 0:
            stack.insert(0, i)
            continue
        while len(stack) != 0 and hist[i] <= hist[stack[0]]:
            stack.pop(0)
        
        if len(stack) != 0 and hist[i] > hist[stack[0]]:
            ans[i] = stack[0]
        stack.insert(0, i)

    return ans


def max_area_histogram(hist):
    n = len(hist)

    next = next_smallest_index(hist, n)

    print(next)
    
    prev = prev_smallest_index(hist, n)

    print(prev)

    max_area = 0
    
    for i in range(0, n):
        length = hist[i]

        if next[i] == -1:
           next[i] = n
        breath = next[i]-prev[i]-1

        area = length * breath
        max_area = max(max_area, area)

    return max_area




if __name__ == '__main__': 
    hist = [2,2,2,2]
    print("Max Area is ", max_area_histogram(hist))