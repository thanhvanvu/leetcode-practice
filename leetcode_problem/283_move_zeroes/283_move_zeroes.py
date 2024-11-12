def moveZeroes(nums):
    i = 0
    l = 0

    while l < len(nums):
        if nums[l] != 0:
            nums[i], nums[l] = nums[l], nums[i]
            i += 1
        l += 1
    return nums


def moveZeroes_practice(nums):
    l = 0
    for r in range(len(nums)):
        if nums[r] != 0:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1

    return nums


nums = [0, 1, 0, 3, 12]

# move all 0's to the end of it while maintaining the relative order
# should understand it different way
# move all number which is != 0 to the front
print(moveZeroes_practice(nums))
