def removeStars(s):
    stack = []

    for char in s:
        if stack and char == "*":
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


s = "erase*****"
print(removeStars(s))