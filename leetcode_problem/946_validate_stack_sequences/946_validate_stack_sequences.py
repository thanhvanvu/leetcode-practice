# https://leetcode.com/problems/validate-stack-sequences/description/


def validateStackSequences(pushed, popped):
    L = 0  # pointer to keep track element in popped
    stack = []

    for num in pushed:
        stack.append(num)

        while stack and stack[-1] == popped[L] and L < len(popped):
            stack.pop()
            L += 1

    if len(stack) == 0:
        return True
    else:
        return False


pushed = [1, 2, 3, 4, 5]
popped = [4, 5, 3, 2, 1]

# stack = []
# loop through pushed and push number in stack
# also check if stack[-1] == popped[L] ? yes -> pop stack, then increment L+=1
# need while loop to check all element popped array

print(validateStackSequences(pushed, popped))
