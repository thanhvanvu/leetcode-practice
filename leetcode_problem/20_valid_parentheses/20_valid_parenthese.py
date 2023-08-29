# https://www.youtube.com/watch?v=WTzjTskDFMg
# https://leetcode.com/problems/valid-parentheses/

def isValid(string):

    # create stack
    stack = []

    # create hash map with every close brackets
    closeToOpen = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    # loop every bracket in the list " ( ) [ } { } "
    for bracket in string:

        # (, {, [ ==> append to stack
        if bracket not in closeToOpen:
            stack.append(bracket)

        # ), }, ] ==> check if (, {, [ is in stack ?? if yes, pop it. No ==> return false
        elif bracket in closeToOpen:

            # stack = [ "{" ] and bracket = "}" => pop
            if stack and stack[-1] == closeToOpen[bracket]:
                stack.pop()
            else:

                # stack = [ "{" ] and bracket = "]" => return False
                return False

    # after append and pop, if stack is empty ==> true
    if len(stack) == 0:
        return True
    else:
        return False


if __name__ == '__main__':
    s = "()[}{}"
    length_arr = len(s)

    a = isValid(s)

    print('isValid', a)
