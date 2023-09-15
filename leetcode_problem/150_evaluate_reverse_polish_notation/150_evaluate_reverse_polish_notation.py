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

tokens = ["4","-2","/","2","-3","-","-"]

print(evalRPN(tokens))
