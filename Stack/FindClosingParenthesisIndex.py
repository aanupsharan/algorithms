def getIndex(expr, location):
    if expr[location] != '[':
        return -1
    
    stack = []

    for i in range(location, len(expr)):
        if expr[i] == '[':
            stack.insert(0,i)
        elif expr[i] == ']':
            stack.pop(0)
        if len(stack) == 0:
                return i

    return -1

def test(expr, location):
    index = getIndex(expr, location)
    print(expr + ", "+ str(location) +" : "+ str(index))

if __name__ == '__main__': 
    expr = "[ABC[EF]][GH]"
    test(expr, 0)