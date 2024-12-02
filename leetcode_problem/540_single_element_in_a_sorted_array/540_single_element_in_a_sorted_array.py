# https://leetcode.com/problems/single-element-in-a-sorted-array/description/
# https://www.youtube.com/watch?v=HGtqdzyUJ3k&t=605s

def singleNonDuplicate_practice(nums):
    count = {}

    for i in range(len(nums)):
        num = nums[i]

        if num not in count:
            count[num] = 1
        else:
            count[num] += 1

    for j in count:
        if count[j] == 1:
            return j


def singleNonDuplicate(nums):
    L = 0
    R = len(nums) - 1

    while L <= R:
        mid = L + (R - L) // 2

        if (mid - 1 < 0 or nums[mid - 1] != nums[mid]) and (mid + 1 == len(nums) or nums[mid] != nums[mid + 1]):
            return nums[mid]

        leftSize = mid - 1 if nums[mid - 1] == nums[mid] else mid

        if leftSize % 2:
            R = mid - 1
        else:
            L = mid + 1


nums = [3, 3, 7, 7, 10, 11, 11]

print(singleNonDuplicate(nums))
