# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/description/

def longestSubarray(nums):
    count0 = 0
    L = 0
    maxLength = float('-inf')

    for R in range(len(nums)):

        num = nums[R]
        if num == 0:
            count0 += 1

        while count0 > 1:
            numL = nums[L]
            if numL == 0:
                count0 -= 1
            L += 1

        window = R - L + 1
        maxLength = max(maxLength, window)

    return maxLength - 1


nums = [1,1,1]
print(longestSubarray(nums))
