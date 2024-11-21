# https://neetcode.io/courses/advanced-algorithms/2
# https://leetcode.com/problems/minimum-size-subarray-sum/description/

def minSubArrayLen(target, nums):
    L = 0
    result = float("inf")
    total = 0

    for R in range(len(nums)):
        total += nums[R]

        while total >= target:
            length = R - L + 1
            result = min(result, length)
            total = total - nums[L]
            L += 1

    return 0 if result == float("inf") else result


def minSubArrayLen_practice(target, nums):
    L = 0
    total = 0
    min_window = float("inf")

    for R in range(len(nums)):
        num = nums[R]
        total = total + num

        # check and keep shrinking window
        # until we find new subarray that meets condition
        while total >= target:
            window = R - L + 1
            min_window = min(window, min_window)

            # shrink window to find new subarray
            total = total - nums[L]
            L += 1

    if min_window == float("inf"):
        return 0
    else:
        return min_window


target = 11
nums = [1,1,1,1,1,1,1,1]

print(minSubArrayLen_practice(target, nums))

# nums = [2,3,1,2,4,3]
# total = 0
# target = 7
# 2 => 0 + 2 = 2
# 3 => 2 + 3 = 5
# 1 => 5 + 1 = 6
# 2 => 6 + 2 = 8 >= target ==> result = length 4
# 8 - 2 = 6
# 4 => 6 + 4 = 10 >= target
# 10 - 3 = 7 >= target ==> result = 3
# 7 - 1 = 6
# 3 => 6 + 3 = 9 >= target
# 9 -2 = 7 >= target ==> result = 2
