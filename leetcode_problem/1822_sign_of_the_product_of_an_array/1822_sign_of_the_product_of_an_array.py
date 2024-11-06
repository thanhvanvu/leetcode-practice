# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# https://www.youtube.com/watch?v=rBENYgWy3xU

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
