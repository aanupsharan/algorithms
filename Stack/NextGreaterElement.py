def createStack():
    stack = []
    return stack

def push(stack,item):
    stack.insert(0,item)

def isEmpty(stack):
    return len(stack) == 0

def pop(stack):
    return stack.pop(0)

def peek(stack):
    if isEmpty(stack):
        return None
    return stack[0]

def printNextGreatestElement(elements):
    n = len(elements)
    ans = (n) * [-1]
    stack = createStack()

    for i in range(n-1, -1, -1):
        
        if isEmpty(stack):
            push(stack, elements[i])
            continue
        
        while len(stack) > 1 and elements[i] >= peek(stack):
            b = pop(stack)

        if not isEmpty(stack) and elements[i] < peek(stack):
            ans[i] = peek(stack)
        push(stack, elements[i])
       
            

    return ans

if __name__ == "__main__":
    elements = [4, 12, 5, 3, 1,2,5,3,1,2,4,6 ]
    
    result = printNextGreatestElement(elements)
    print(elements)
    print(result)

