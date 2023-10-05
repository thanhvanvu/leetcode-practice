def moveZeroes(nums):
    i = 0
    l = 0

    while l < len(nums):
        if nums[l] != 0:
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
        l += 1
    return nums


nums = [0]
print(moveZeroes(nums))
