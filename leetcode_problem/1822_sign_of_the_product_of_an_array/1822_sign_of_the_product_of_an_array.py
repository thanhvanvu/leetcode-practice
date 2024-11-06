# https://leetcode.com/problems/sign-of-the-product-of-an-array/description/

# if we see 0 --> return 0
# product will always be positive if we have even number of "-": example: 2 number of -1, 4 number of -2
# product will always be negative if we have odd number of "-"
# just count negative number and return
def arraySign(nums):
    negative = 0

    for i in nums:
        if i == 0:
            return 0

        if i < 0:
            negative += 1

    if negative % 2 == 0:
        return 1
    else:
        return -1


def arraySign1(nums):
    product = 1

    for i in nums:
        product *= i

    if product < 0:
        return -1
    elif product == 0:
        return 0
    else:
        return 1


lst = [-1, 1, -1, 1, -1]
print(arraySign(lst))
