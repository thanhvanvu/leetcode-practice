# https://leetcode.com/problems/crawler-log-folder/description/

def minOperations(logs):
    stack = []
    for operation in logs:
        if operation != "./" and operation != "../":
            stack.append(operation)
        elif operation == "./":
            continue
        elif stack and operation == "../":
            stack.pop()

    return len(stack)


logs = ["d1/", "../", "../", "../"]
print(minOperations(logs))

# everytime we pop something from stack, need to check if stack is empty or not

# ["d1/","d2/","../","d21/","./"]
# d1/                       => stack [d1/]
# d1/, d2/                  => stack [d1/, d2/]
# d1/, d2/, ../ => pop => stack [d1/]
# d1/, d2/, ../, d21        => stack [d1/, d21/]
# d1/, d2/, ../, d21, ./ => do nothing

# minimum of operations needed to go back to the main folder is len(stack)
