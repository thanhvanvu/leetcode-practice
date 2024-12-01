# https://leetcode.com/problems/squares-of-a-sorted-array/description/
# https://www.youtube.com/watch?v=FPCZsG_AkUg

# easy solution
def sortedSquares(nums):
    for i in range(len(nums)):
        nums[i] = nums[i] ** 2

    nums.sort()

    return nums


def sortedSquares_2pointer(nums):
    L = 0
    R = len(nums) - 1
    result = [0] * len(nums)

    for i in range(len(result) - 1, -1, -1):
        while L <= R:
            left = nums[L] ** 2
            right = nums[R] ** 2

            if left >= right:
                result[i] = left
                L += 1
                break
            else:
                result[i] = right
                R -= 1
                break
    return result


# cleaner version
def sortedSquares_2pointer_cleaner(nums):
    L = 0
    R = len(nums) - 1
    result = []

    while L <= R:
        left = nums[L] ** 2
        right = nums[R] ** 2

        if left >= right:
            result.append(left)
            L += 1
        else:
            result.append(right)
            R -= 1

    return result[::-1]  # reverse


# two pointer
# we want to build the R^2 reverse order
# -4^2 compare 10^2 -> 16 < 100
# [.., .., .., .., .., 100]
# shift pointer
# -4^2 compare 3^2 -> 16 > 9
# [.., .., .., .., 16, 100]
# shift pointer
# -1^2 compare 3^2 -> 1 < 9
# [.., .., .., 9, 16, 100]
# so on and so on

nums = [-4, -1, 0, 3, 10]
print(sortedSquares_2pointer_cleaner(nums))
