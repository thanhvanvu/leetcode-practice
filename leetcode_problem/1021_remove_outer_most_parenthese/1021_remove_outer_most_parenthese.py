# https://leetcode.com/problems/remove-outermost-parentheses/description/

def removeOuterParentheses(s):
    stackSave = []  # pair: [parentheses, index]
    stringOutput = ""

    for i, par in enumerate(s):
        if par == "(":
            stackSave.append([par, i])
        else:
            paren, index = stackSave.pop()

            if len(stackSave) == 0:
                stringOutput += s[index + 1: i]

    return stringOutput


s = "(()())(())"
print(removeOuterParentheses(s))

# stack = []
# ( ==>             stack = [ ( ]
# ( ( ==>           stack = [ (, ( ]
# ( ( ) ==>         pop top ==> [ ( ]
# ( ( ) ( ==>       stack = [ (, ( ]
# ( ( ) ( ) ==>     pop top ==> [ ( ]
# ( ( ) ( ) ) ==>   pop top ==> [ ]
# check if len(stack) == 0
# => append the result without outermost parentheses
# result = ( ) ( )
