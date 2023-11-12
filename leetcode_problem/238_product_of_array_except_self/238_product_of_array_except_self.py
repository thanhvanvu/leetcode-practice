from math import prod


def productExceptSelf_memory(nums):
    preFix = []
    postFix = [0] * len(nums)
    output = []

    prod_pre = 0
    prod_post = 0
    result = 0
    for i in range(len(nums)):
        if i == 0:
            prod_pre = nums[i]

        else:
            prod_pre *= nums[i]
        preFix.append(prod_pre)

    for i in range(len(nums) - 1, -1, -1):
        if i == len(nums) - 1:
            prod_post = nums[i]
        else:
            prod_post *= nums[i]
        postFix[i] = prod_post

    for i in range(len(nums)):
        if i == 0:
            result = 1 * postFix[i + 1]
        elif i == len(nums) - 1:
            result = 1 * preFix[i - 1]
        else:
            result = preFix[i - 1] * postFix[i + 1]

        output.append(result)

    return output


# O(n) time complexity
# O(1) space complexity
def productExceptSelf(nums):
    result = [1] * len(nums)

    prefix = 1
    for i in range(len(nums)):
        result[i] = prefix
        prefix = nums[i] * prefix

    postfix = 1
    for i in range(len(nums) - 1, -1, -1):
        result[i] = result[i] * postfix
        postfix = postfix * nums[i]

    return result


nums = [1, 2, 3, 4]
print(productExceptSelf(nums))
