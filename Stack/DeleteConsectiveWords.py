def deleteConsectiveWords(sentence):
    stack = []

    words = sentence.split()

    print(words)
    for i in range(len(words)):
        if len(stack) > 0:
            if words[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(words[i])
        else:
            stack.append(words[i])
    return len(stack)  
        
if __name__ == "__main__":
    sentence = "tom jerry jerry tom"
    result = deleteConsectiveWords(sentence)

    print("result :: ", result)