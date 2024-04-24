import math

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
    return stack[0]

def deleteMiddleofStack(stack):

    n = len(stack)
    mid = math.floor(n/2)
    print(mid)
    tmpStack = createStack()
    for i in range(0, n):
        element = pop(stack)
        if i == mid-1:
            break
        else:
            push(tmpStack, element)

    while not isEmpty(tmpStack):
        push(stack, pop(tmpStack))

    return stack

if __name__ == "__main__":
    stack = createStack()

    push(stack, 4)
    push(stack, 2)
    push(stack, 1)
    push(stack, 3)
    push(stack, 5)
    push(stack, 7)

    print(stack)

    deleteMiddleofStack(stack)

    print(stack)