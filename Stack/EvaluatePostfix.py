def evaluatePostfix(expr):
    stack = []
    for i in range(len(expr)):
        c = expr[i]

        if c.isnumeric():
            stack.append(c)
        else:
            second = float(stack.pop())
            first = float(stack.pop())

            if c == '^':
                first = pow(first, second)
            elif c == '/':
                first = first / second
            elif c == '*':
                first = first * second
            elif c == '-':
                first = first - second
            elif c == '+':
                first = first + second
            
            stack.append(first)
    
    return stack.pop()

if __name__ == "__main__":
    expr = "231*+9-"
    result = evaluatePostfix(expr)
    print(result)