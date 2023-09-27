def search(nums, target):
    l = 0
    r = len(nums) - 1

    while l <= r:
        m = l + ((r - l) // 2)  # (l + r) // 2 can lead to overflow

        if target < nums[m]:
            r = m - 1
        elif target > nums[m]:
            l = m + 1

        if nums[m] == target:
            return m

    return -1


array = [-1, 0, 3, 5, 9, 12]
value = 2

print(search(array, value))
