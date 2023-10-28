# https://leetcode.com/problems/make-the-string-great/submissions/

def makeGood(s):
    stack = []
    for i in s:
        if stack and ((i.isupper() and i.lower() == stack[-1]) or (stack[-1].isupper() and stack[-1].lower() == i)):
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)


s = "s"
print(makeGood(s))

# aB
# check if B is upperCase and B.lower() == a
# i.isupper() and i.lower() == stack[-1]

# Cd
# check if C is upperCase and C.lower() == d
# stack[-1].isupper() and stack[-1].lower() == i
