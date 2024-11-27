# https://leetcode.com/problems/remove-k-digits/description/
# https://www.youtube.com/watch?v=cFabMOnJaq0

def removeKdigits(num, k):
    stack = []

    # pop() if:
    # 1/ if stack not empty
    # 2/ n < stack[-1], because we want monotonic increasing order 12345
    # 3/ k > 0

    for n in num:
        while stack and n < stack[-1] and k > 0:
            stack.pop()
            k -= 1

        stack.append(n)

    # edge case
    # [1,2,3,4,5,6], k=3
    # just remove last 3 in the stack
    length = len(stack) - k
    stack = stack[:length]

    # Convert stack back to a string and remove leading zeros
    res = "".join(stack).lstrip('0')

    # If result is empty after removing leading zeros, return "0"
    return res if res else "0"


# monotonic increasing
# append number to stack
# if number < stack[-1] --> pop(), k -= 1
# using while to check if number < stack[-1]
# if yes -> pop(), k -= 1
# if k = 0, stop checking
num = "1432219"
k = 3
print(removeKdigits(num, k))
