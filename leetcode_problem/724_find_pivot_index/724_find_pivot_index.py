# https://leetcode.com/problems/find-pivot-index/description/
# https://www.youtube.com/watch?v=7yF-U1hLEqQ
import math


def pivotIndex(nums):
    sumTotal = sum(nums)
    leftSum = 0

    # [1, 7, 3, 6, 5, 6]
    # i = 0, rightSum = 28 - 0 - 1 = 27, leftSum # rightSum -> leftSum =+ nums[i] = 1
    # i = 1, rightSum = 28 - leftSum - nums[i] = 28 - 1 - 7 = 20, leftSum # rightSum -> leftSum = 1 + 7 = 8
    # ...
    for i, val in enumerate(nums):
        rightSum = sumTotal - leftSum - val

        # 2 sum from 2 side need to be equivalent -> pivot
        if leftSum == rightSum:
            return i
        else:
            # update leftSum
            leftSum = leftSum + val

    # if for loop is done -> no pivot
    return -1


lst = [1, 7, 3, 6, 5, 6]
print(pivotIndex(lst))
