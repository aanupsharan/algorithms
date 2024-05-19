def calculateSpan(price, n):
    if n == 0:
        return None
    
    stack = []
    ans = n * [1]
    for i in range(0, n):
        while len(stack) != 0 and price[i] > price[stack[0]]:
            stack.pop(0)
        
        ans[i] = i - stack[0] if len(stack) > 0 else i + 1
        stack.insert(0, i)

    return ans


if __name__ == "__main__":
    price = [100, 80, 60, 70, 60, 75, 85]
    #price = [10, 4, 5, 90, 120, 80]
    print(calculateSpan(price, len(price)))
