def prec(c):
    if c == '^':
        return 3
    elif c == '/' or c == '*':
        return 2
    elif c == '+' or c == '-':
        return 1
    else:
        return -1
def associativity(c):
    if c == '^':
        return 'R'
    return 'L'

def postfix(expr):

    expr = "(" +expr+ ")"
    stack = []
    result = []

    for i in range(len(expr)):
        if expr[i].isnumeric():
            result.append(expr[i])
        elif expr[i] == '(':
            stack.append(expr[i])
        elif expr[i] == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            while len(stack) > 0 and (prec(expr[i]) < prec(stack[-1]) or 
                                     (prec(expr[i]) == prec(stack[-1]) and associativity(expr[i]) == 'L')):
                result.append(stack.pop())
            stack.append(expr[i])
    
    while len(stack) != 0:
        result.append(stack.pop())
    
    return ''.join(result)


def evaluate(expr):
    postfixNotation = postfix(expr)
    stack = []
    for i in range(len(postfixNotation)):
        c = postfixNotation[i]
        if c.isnumeric():
            stack.append(c)
        else:
            second = float(stack.pop())
            first = float(stack.pop())
            if c == '+':
                first = first + second
            elif c == '-':
                first = first - second
            elif c == '*':
                first = first * second
            elif c == '/':
                first = first / second
            elif c == '^':
                first = pow(first, second)
            stack.append(first)

    return stack.pop()
            


if __name__ == "__main__":
    expr = "(2+4)*(4+6)"
    result = evaluate(expr)
    print(result)
