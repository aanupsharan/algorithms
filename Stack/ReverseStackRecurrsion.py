def createStack():
    stack = []
    return stack

def push(stack,item):
    stack.append(item)

def isEmpty(stack):
    return len(stack) == 0

def pop(stack):
    return stack.pop()

def insertInBottom(stack, item):
    if isEmpty(stack):
        push(stack, item)
    else:
        temp = pop(stack)
        insertInBottom(stack, item)
        push(stack, temp)

def reverse(stack):
    if isEmpty(stack):
        return
    else:
        temp = pop(stack)
        reverse(stack)
        insertInBottom(stack, temp)

if __name__ == "__main__":
    stack = createStack()
    push(stack, 1)
    push(stack, 2)
    push(stack, 3)
    push(stack, 4)

    reverse(stack)

    print(stack)