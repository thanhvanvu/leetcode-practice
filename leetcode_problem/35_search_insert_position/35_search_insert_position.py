# https://leetcode.com/problems/search-insert-position/description/


def search_practice(nums, target):
    L = 0
    R = len(nums) - 1
    mid = 0
    while L <= R:
        mid = L + (R - L) // 2

        if nums[mid] < target:
            L = mid + 1
        elif nums[mid] > target:
            R = mid - 1
        else:
            return mid

    # [1, 3, 5, 6]
    # target = 0
    # after checking, cant find 0 in array and mid = 0
    # check if target > nums[mid] -> return mid + 1
    # else return mid
    if target > nums[mid]:
        return mid + 1
    else:
        return mid



array = [1, 3, 5, 6]
value = 5

print(search_practice(array, value))
