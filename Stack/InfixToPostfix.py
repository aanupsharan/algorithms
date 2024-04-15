def prec(s):
    if s == '^':
        return 3
    elif s == '*' or s == '/':
        return 2
    elif s == '+' or s == '-':
        return 1
    else:
        return -1

def associativity(s):
    if s == '^':
        return 'R'
    return 'L'

def infixToPostfix(expr):
    result = []
    stack = []

    for i in range(len(expr)):
        
        c = expr[i]
        if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9') :
            result.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while len(stack) > 0 and stack[-1] != '(':
                result.append(stack.pop())
            stack.pop()
        else:
            if len(stack) == 0:
                stack.append(c)
                continue
            while len(stack) > 0 and (prec(c) < prec(stack[-1]) or 
                                     (prec(c) == prec(stack[-1]) and associativity(c) == 'L')):
                result.append(stack.pop())
            stack.append(c)
    
    while len(stack) > 0:
        result.append(stack.pop())

    return result
if __name__ == "__main__":
    expr = "a+b*(c^d-e)^(f+g*h)-i"

    result = infixToPostfix(expr)
    print(''.join(result))