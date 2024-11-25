# https://leetcode.com/problems/make-the-string-great/submissions/

def makeGood(s):
    stack = []
    for i in s:
        if stack and ((i.isupper() and i.lower() == stack[-1]) or (stack[-1].isupper() and stack[-1].lower() == i)):
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)


def makeGood_practice(s):
    stack = []

    for char in s:
        if stack and char == stack[-1]:
            stack.append(char)
        elif stack and char.lower() == stack[-1]:
            stack.pop()
        elif stack and char.upper() == stack[-1]:
            stack.pop()
        else:
            stack.append(char)

    return "".join(stack)


s = "leEeetcode"
print(makeGood_practice(s))

# aB
# check if B is upperCase and B.lower() == a
# i.isupper() and i.lower() == stack[-1]

# Cd
# check if C is upperCase and C.lower() == d
# stack[-1].isupper() and stack[-1].lower() == i
