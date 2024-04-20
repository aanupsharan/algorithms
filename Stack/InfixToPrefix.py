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

def infixToPostfix(infix):
    infix = '(' + infix + ')'
    stack = []
    postfix = []

    for i in range(len(infix)):
        if infix[i].isalpha() or infix[i].isnumeric():
            postfix.append(infix[i])
        elif infix[i] == '(':
            stack.append(infix[i])
        elif infix[i] == ')':
            while stack[-1] != '(':
                postfix.append(stack.pop())
            stack.pop()
        else:
            while prec(infix[i]) < prec(stack[-1]) or (prec(infix[i]) == prec(stack[-1]) and associativity(infix[i])):
                postfix.append(stack.pop())
            stack.append(infix[i])

    while len(stack) != 0:
        postfix.append(stack.pop())
    
    return postfix

def infixToPrefix(infix):
    l = len(infix)

    infix = infix[::-1]

    infix = list(infix)
    for i in range(l):
        if infix[i] == '(':
            infix[i] = ')'
        elif infix[i] == ')':
            infix[i] = '('
    
    infix = ''.join(infix)
    postfix = infixToPostfix(infix)
    prefix = postfix[::-1]
    return prefix

if __name__ == "__main__":
    expr = "x+y*z/w+u"
    result = infixToPrefix(expr)
    print(''.join(result))