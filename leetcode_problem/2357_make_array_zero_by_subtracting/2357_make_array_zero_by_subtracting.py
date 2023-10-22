# https://leetcode.com/problems/make-array-zero-by-subtracting-equal-amounts/description/

import heapq


def minimumOperations(nums):
    # transform list to heap
    heapq.heapify(nums)
    count = 0

    while True:

        # pop minimum value
        minimum = heapq.heappop(nums)

        # if min == 0, continue popping until we got non-0 value
        if minimum != 0:

            # subtract every value by min
            for i in range(len(nums)):
                nums[i] = nums[i] - minimum

            # count the operation
            count += 1

        # check if length of array == 0
        # break loop
        if len(nums) == 0:
            break

    return count


nums = [1, 5, 0, 3, 5]

print(minimumOperations(nums))
