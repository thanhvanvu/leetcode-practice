# https://leetcode.com/problems/largest-3-same-digit-number-in-string/description/
# https://www.youtube.com/watch?v=vcrOpJQHsSE

# def largestGoodInteger(num):
#     count = 0
#     k = 0
#     result = ""
#     substring = ""
#
#     for i in range(len(num)):
#         temp = num[i]
#         if num[i] == num[k]:
#             count += 1
#             substring += num[i]
#
#             if count == 3:
#                 result = max(int(result), int(substring))
#                 substring = ""
#                 count = 0
#         else:
#             k = i
#             substring = ""
#             count = 1
#
#     return result

# using stack
def largestGoodInteger_stack(num):
    stack = []
    maxOutput = float("-inf")
    for i in range(len(num)):
        val = num[i]

        if len(stack) == 0 or (val == stack[0]) and len(stack) < 3:
            stack.append(val)

            if len(stack) == 3:
                result = "".join(stack)
                maxOutput = max(int(result), maxOutput)
        else:
            stack = [val]

    if maxOutput == float("-inf"):
        return ""
    else:
        if maxOutput == 0:
            return f"{maxOutput:03}"
        else:
            return str(maxOutput)


def largestGoodInteger(num):
    maxOutput = "0"

    # compare i, i+1, i+2,
    # so we stop at len(num)-2 -> I will not be out of bound
    for i in range(len(num) - 2):
        if num[i] == num[i + 1] == num[i + 2]:
            string = num[i: i + 3]
            maxOutput = max(maxOutput, string)

    # if for loop is done and maxOutput still = "0"
    # meaning no 3 same digit -> return ""

    return "" if maxOutput == "0" else maxOutput


txt = "42352338"
print(largestGoodInteger(txt))
