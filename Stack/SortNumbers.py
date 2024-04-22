def createStack():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)

def isEmpty(stack):
    return len(stack) == 0

def pop(stack):
    return stack.pop()

def peek(stack):
    return stack[-1]

def sort(stack):
    tmpStack = createStack()

    while len(stack) != 0:
        temp = pop(stack)

        while len(tmpStack) > 0 and temp > peek(tmpStack):
            push(stack, pop(tmpStack))
        
        push(tmpStack, temp)

    return tmpStack

if __name__ == "__main__":
    stack = createStack()
    push(stack, 4)
    push(stack, 2)
    push(stack, 1)
    push(stack, 3)
    push(stack, 5)

    result = sort(stack)

    print(result)

