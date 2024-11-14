# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/description/
# https://www.youtube.com/watch?v=ycAq8iqh0TI

def removeDuplicates(nums):
    count = {}  # number: count

    L = 0

    for R in range(len(nums)):
        number = nums[R]
        if number not in count:
            count[number] = 1
            nums[L] = nums[R]
            L += 1
        else:
            if count[number] >= 2:
                continue
            else:
                count[number] += 1
                nums[L] = nums[R]
                L += 1

    return L


def removeDuplicates_practice(nums):
    if len(nums) <= 2:
        return len(nums)

    index = 2

    for i in range(2, len(nums)):

        if nums[i] != nums[index - 1] or nums[i] != nums[index - 2]:
            nums[index] = nums[i]
            index += 1

    return index


nums = [1, 1, 1, 2, 2, 3]
print(removeDuplicates_practice(nums))
