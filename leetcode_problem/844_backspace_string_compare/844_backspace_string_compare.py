# https://leetcode.com/problems/backspace-string-compare/description/

def backspaceCompare(s, t):
    stackS = []
    stackT = []

    for i in s:
        if i != "#":
            stackS.append(i)
        else:
            if stackS:
                stackS.pop()
            else:
                continue

    for i in t:
        if i != "#":
            stackT.append(i)
        else:
            if stackT:
                stackT.pop()
            else:
                continue

    return True if stackS == stackT else False
    # j = len(t) - 1
    #
    # while j >= 0:
    #     if t[j] != "#":
    #         if t[j] == stack[-1]:
    #             stack.pop()
    #             j -= 1
    #         else:
    #             return False
    #     else:
    #         j -= 2
    #
    # return True


def backspaceCompare_practice(s,t):
    stack_s =[]
    stack_t = []

    for c in s:
        if c == "#" and len(stack_s) > 0:
            stack_s.pop()

        if c != "#":
            stack_s.append(c)

    for c in t:
        if c == "#" and len(stack_t) > 0:
            stack_t.pop()

        if c != "#":
            stack_t.append(c)

    return True if stack_s == stack_t else False

s = "a#c"
t = "b"
print(backspaceCompare_practice(s, t))
