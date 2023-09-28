# https://www.youtube.com/watch?v=sEQk8xgjx64
# https://leetcode.com/problems/sort-colors/description/


def sortColors(nums):
    low = 0  # track 0
    high = len(nums) - 1  # track 2
    mid = 0

    # loop through the entire of array
    # if see 2, swap it with "high" pointer => high -= 1
    # if see 0, swap it with "low" pointer => low += 1, mid += 1
    # if see 1 => mid += 1
    while mid <= high:
        if nums[mid] == 0:
            nums[low], nums[mid] = nums[mid], nums[low]
            low += 1
            mid += 1
        elif nums[mid] == 1:
            mid += 1
        else:
            nums[mid], nums[high] = nums[high], nums[mid]
            high -= 1
    return nums


nums = [2, 0, 2, 1, 1, 1, 0]
print(sortColors(nums))
