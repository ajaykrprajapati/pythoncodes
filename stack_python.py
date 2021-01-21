def createstack():
    stack = []
    return stack

def size(stack):
    return len(stack)

def isEmpty(stack):
    return size(stack) == 0

def push(stack, item):
    stack.append(item)

def pop(stack):
    if isEmpty(stack): return
    return stack.pop()

def reverse(str):
    stack = createstack()
    length = len(str)

    for i in range(0, length):
        push(stack, str[i])
    stringg =""
    for i in range(0, length):
        stringg += pop(stack)
    print(stringg)


if __name__ == "__main__":
    reverse("my name is ajay")