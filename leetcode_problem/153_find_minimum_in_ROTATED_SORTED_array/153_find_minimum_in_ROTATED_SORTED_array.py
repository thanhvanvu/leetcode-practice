# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/

def findMin(nums):
    l = 0
    r = len(nums) - 1

    minimum = nums[0]

    while l <= r:
        mid = (l + r) // 2

        # compare mid value with minimum
        minimum = min(minimum, nums[mid])

        # mid > right ==> search right
        if nums[mid] > nums[r]:
            l = mid + 1

        # mid <= right ==> search left
        elif nums[mid] <= nums[r]:
            r = mid - 1

    return minimum


# [4, 5, 6, 7] > [0, 1, 2]

nums = [4, 5, 6, 7, 0, 1, 2]

print(findMin(nums))
