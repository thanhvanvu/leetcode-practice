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


def isValid_practice(s):
    stack = []
    parentheses = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for char in s:
        # if stack not empty
        # and char is in hashmap
        # check the last parenthe in hashmap
        if stack and char in parentheses:
            last_char = stack[-1]
            if last_char == parentheses[char]:
                stack.pop()
            else:
                # return False immediately
                # if do not see the match
                return False

        if char not in parentheses:
            stack.append(char)

    if len(stack) > 0:
        return False
    else:
        return True


if __name__ == '__main__':
    s = "(])"
    length_arr = len(s)

    a = isValid_practice(s)

    print('isValid', a)
