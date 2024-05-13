def reverse(num):
    stack = []

    while num != 0:
        stack.append(num % 10)
        num = int(num / 10)
    
    sum = 0
    while len(stack) != 0:
        sum = sum * 10 + stack.pop(0)
    
    return sum


if __name__ == "__main__":
    number = 3678
    rev = reverse(number)
    print(rev)
