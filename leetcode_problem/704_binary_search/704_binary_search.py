def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow

        # loop first half
        if target < nums[m]:
            r = m - 1

        # loop second half
        elif target > nums[m]:
            l = m + 1

        if nums[m] == target:
            return m

    return -1


def search_practice(nums, target):
    L = 0
    R = len(nums) - 1

    while L <= R:

        mid = L + (R - L) // 2

        if nums[mid] > target:
            R = mid - 1
        elif nums[mid] < target:
            L = mid + 1
        else:
            return mid

    return -1


array = [-1, 0, 3, 5, 9, 12]
value = 9

print(search_practice(array, value))
