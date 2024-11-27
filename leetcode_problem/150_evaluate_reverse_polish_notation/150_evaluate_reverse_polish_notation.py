# https://leetcode.com/problems/evaluate-reverse-polish-notation/description/
# https://www.youtube.com/watch?v=iu0082c4HDE

def evalRPN(tokens):
    stack = []
    result = 0
    for i in tokens:
        if i == "+":
            result = stack.pop(-2) + stack.pop(-1)
            stack.append(result)
        elif i == "-":
            result = stack.pop(-2) - stack.pop(-1)
            stack.append(result)
        elif i == "*":
            result = stack.pop(-2) * stack.pop(-1)
            stack.append(result)
        elif i == "/":
            first = stack.pop(-2)
            second = stack.pop(-1)

            result = first / second
            stack.append(int(result))

        else:
            stack.append(int(i))

    return stack[-1]


def evalRPN_practice(tokens):
    stack = []
    for t in tokens:
        if t == "+":
            result = int(stack.pop()) + int(stack.pop())
            stack.append(result)
        elif t == "-":
            a = int(stack.pop())
            b = int(stack.pop())
            result = b - a
            stack.append(result)
        elif t == "*":
            result = int(stack.pop()) * int(stack.pop())
            stack.append(result)
        elif t == "/":
            a = int(stack.pop())
            b = int(stack.pop())
            result = b / a
            stack.append(int(result))
        else:
            stack.append(t)

    return stack[-1]


tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]

print(evalRPN_practice(tokens))
