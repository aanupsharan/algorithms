def isBracketsBalanced(expr):
    if expr == None:
        return True
    
    stack = []

    for i in range(len(expr)):
        if expr[i] == '[' or expr[i] == '(' or expr[i] == '{':
            stack.append(expr[i])
        else:
            if (expr[i] == ']' and stack[-1] != '[') or (expr[i] == '(' and stack[-1] != ')') or (expr[i] == '{' and stack[-1] != '}'):
                return False
            else:
                stack.pop()

    if len(stack) != 0:
        return False

    return True

if __name__ == "__main__":
    expr = "[()]{}{[()()]()}"
    
    if isBracketsBalanced(expr):
        print("Brackets are balanced")
    else:
        print("Brackets are not balanced")

    