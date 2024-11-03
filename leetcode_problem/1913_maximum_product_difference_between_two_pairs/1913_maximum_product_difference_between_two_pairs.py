# https://leetcode.com/problems/maximum-product-difference-between-two-pairs/description/
# https://www.youtube.com/watch?v=wBPoEm3r3EA
import heapq


def maxProductDifference1(nums):
    # (a * b) - (c * d)
    # to make maximum product
    # a, b must be 2 largest number
    # c, d must be 2 smallest number

    nums = sorted(nums)
    print(nums)

    a, b = nums[-1], nums[-2]
    c, d = nums[0], nums[1]

    return (a * b) - (c * d)


def maxProductDifference_heap(nums):
    # transform list to heap
    heapq.heapify(nums)

    # c, d are smallest number
    c, d = (heapq.heappop(nums)), (heapq.heappop(nums))

    # because we need maxHeap but python only has minHeap
    # => convert array to negative
    # transform list to heap
    for i in range(len(nums)):
        nums[i] *= (-1)

    # transform list to heap
    heapq.heapify(nums)

    # a, b are largest number
    a, b = abs(heapq.heappop(nums)), abs(heapq.heappop(nums))

    return (a * b) - (c * d)


def maxProductDifference(nums):
    max1 = max2 = 0
    min1 = min2 = float("inf")

    for n in nums:
        if n > max2:
            if n > max1:
                max1, max2 = n, max1
            else:
                max2 = n

        if n < min2:
            if n < min1:
                min1, min2 = n, min1
            else:
                min2 = n

    return (max1 * max2) - (min1 * min2)


lst = [4, 2, 5, 9, 7, 4, 8]

print(maxProductDifference(lst))
