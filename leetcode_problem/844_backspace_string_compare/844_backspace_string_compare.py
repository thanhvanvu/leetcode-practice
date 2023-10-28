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


s = "a##c"
t = "#a#c"
print(backspaceCompare(s, t))
