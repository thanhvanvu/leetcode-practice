# https://leetcode.com/problems/decode-string/description/
# https://www.youtube.com/watch?v=qB0zZpBJlh8

def decodeString(s: str):
    stack = []

    for char in s:

        stack.append(char)

        if char == "]":
            # pop "]" out of stack
            stack.pop()

            # build content inside []
            content = ""
            while stack and stack[-1] != "[":
                content = stack[-1] + content
                stack.pop()

            # pop "[" out of stack
            stack.pop()

            # build number before [
            number = ""
            while stack and stack[-1].isnumeric():
                number = stack[-1] + number
                stack.pop()

            result = int(number) * content

            stack.append(result)

    return "".join(stack)


# guarantee the number will always before [
# loop through the string
# append everything until we meet "]"
# pop everything until we see "["  => content
# before "[" will be the number, but the number might be more than 2 digit (11 ~...)
# Need to use WHILE loop to build all string number
# result = number * content
# append result to stack.
# continue from step 1
s = "2[abc]3[cd]ef"
print(decodeString(s))
