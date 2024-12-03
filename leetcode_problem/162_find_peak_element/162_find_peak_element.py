# https://leetcode.com/problems/find-peak-element/description/
# https://www.youtube.com/watch?v=kMzJy9es7Hc&t=645s

def findPeakElement(nums):
    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = L + (R - L) // 2
        if mid > 0 and nums[mid - 1] > nums[mid]:
            R = mid - 1
        elif mid < len(nums) - 1 and nums[mid + 1] > nums[mid]:
            L = mid + 1
        else:
            return mid


nums = [1, 2, 1, 3, 5, 6, 4]
# find mid = 3 => value = 3
# check neighbor
# in case out of bound, need to check if mid > 0, mid < len(nums) - 1
# if nums[mid - 1] > 3 => search left
# if nums[mid + 1] > 3 => search right
print(findPeakElement(nums))
