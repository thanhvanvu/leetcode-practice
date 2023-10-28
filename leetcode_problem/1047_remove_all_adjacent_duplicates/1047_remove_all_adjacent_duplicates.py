# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/

def removeDuplicates(s):
    stack = []

    for i in s:
        if stack and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)

    return "".join(stack)


s = "azxxzy"
print(removeDuplicates(s))

# s = "azxxzy"
# stack = []
# a => stack = [a]
# az => stack = [a, z]
# azx => stack = [a, z, x]
# azxx => duplicate x => pop => stack = [a, z]
# azxxz => duplicate z => pop => stack = [a]
# azxxzy => [a, y]
# combine stack and return
