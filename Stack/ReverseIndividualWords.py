def reverse(sentence):
    if sentence == None:
        return sentence
    
    stack = []
    result = []

    for i in range(len(sentence)):
        if sentence[i] != ' ':
            stack.append(sentence[i])
        else:
            while len(stack) != 0:
                result.append(stack.pop())
            result.append(sentence[i])

    while len(stack) != 0:
        result.append(stack.pop())
        
    return ''.join(result)


if __name__ == "__main__":
    sentence = "my name is anup"
    result = reverse(sentence)

    print(result)