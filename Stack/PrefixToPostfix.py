def isOperator(c):
    if c == '+' or c == '-' or c == '*' or c == '/' or c == '^' or c == '(' or c == ')' :
        return True
    return False

def prefixToPostfix(expr):

    stack = []
    i = len(expr) - 1

    while i >= 0:
        if isOperator(expr[i]):
            temp = stack.pop() + stack.pop() + expr[i]
            stack.append(temp)
        else:
            stack.append(expr[i])    
        i -= 1

    return stack.pop()

if __name__ == "__main__":
    expr = "*-A/BC-/AKL"

    result = prefixToPostfix(expr)
    print(result)