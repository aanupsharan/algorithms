def isOperator(c):
    if c == '+' or c == '-' or c == '*' or c == '/' or c == '^' or c == '(' or c == ')' :
        return True
    return False

def postfixtoPrefix(expr):
    stack = []
    
    for i in range(len(expr)):
        if isOperator(expr[i]):
            second = stack.pop()
            first = stack.pop()
            temp =  expr[i] + first + second
            stack.append(temp)
        else:
            stack.append(expr[i])

    return stack.pop()

if __name__ == "__main__":
    expr = "ABC/-AK/L-*"

    result = postfixtoPrefix(expr)
    print(result)