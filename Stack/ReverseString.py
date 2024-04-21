def reverse(word):
    if word == None:
        return

    stack = []
    result = []
    
    for i in range(len(word)):
        stack.append(word[i])

    for i in range(len(stack)):
        result.append(stack.pop())

    
    return ''.join(result)

if __name__ == "__main__":
    word = "Hello world"
    result = reverse(word)

    print(result)
