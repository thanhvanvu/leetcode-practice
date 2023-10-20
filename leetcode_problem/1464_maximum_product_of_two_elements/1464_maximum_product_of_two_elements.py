# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/

import heapq


def maxProduct(nums):

    nums = [-x for x in nums]

    # transform list to heap
    heapq.heapify(nums)

    # get biggest and second-biggest value
    first = heapq.heappop(nums)
    second = heapq.heappop(nums)


    return (abs(first) - 1) * (abs(second) - 1)


nums = [1, 5, 4, 5]
print(maxProduct(nums))
