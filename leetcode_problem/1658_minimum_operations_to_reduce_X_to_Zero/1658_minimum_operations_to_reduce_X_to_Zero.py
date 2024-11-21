# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/description/
# https://www.youtube.com/watch?v=xumn16n7njs


def minOperations(nums, x):
    total = sum(nums)
    target = total - x

    # now find the window that sum up to y
    L = 0
    sum_total = 0
    max_output = -1
    for R in range(len(nums)):
        sum_total += nums[R]

        # shrinking window
        while L <= R and sum_total > target:
            sum_total -= nums[L]
            L += 1

        if sum_total == target:
            window = R - L + 1
            max_output = max(max_output, window)

    return -1 if max_output == -1 else len(nums) - max_output


nums = [3, 2, 20, 1, 1, 3]
x = 10
# find the minimum window that sum up to x = 5
# to solve this problem, think reversely
# [1, 1, 4, 2, 3] -> total = 11
# 11 - 5 = 6
# find the longest window that sum up to 6
# [1, 1, 4]  = 3
# [4, 2] = 2
# length - longest window = 5 - 3 = 2
# --> return 2 is minimum of operation
print(minOperations(nums, x))
