# https://leetcode.com/problems/find-subsequence-of-length-k-with-the-largest-sum/description/


def maxSubsequence(nums, k):
    # sort decensing order
    nums_sorted = sorted(nums, reverse=True)
    hashNum = {}  # hashmap
    result = []  # result

    # count number and put it hash map
    # {39: 1, 38: 3, 36: 1, 35: 2, 34: 1}
    for i in range(0, k):
        if nums_sorted[i] not in hashNum:
            hashNum[nums_sorted[i]] = 1
        else:
            hashNum[nums_sorted[i]] += 1

    # loop through original array
    # check the value if it is in hashmap ==> append into [result]
    # also remove that value from hashmap, so we dont see it again
    for i in range(len(nums)):
        if nums[i] in hashNum and hashNum[nums[i]] > 0:
            result.append(nums[i])
            hashNum[nums[i]] -= 1

        if len(result) == k:
            break

    return result


nums = [-16, -13, 8, 16, 35, -17, 30, -8, 34, -2, -29, -35, 15, 13, -30, -34, 6, 15, 28, -23, 34, 28, -24, 15, -17, 10,
        31, 32, -3, -36, 19, 31, -5, -21, -33, -18, -23, -37, -15, 12, -28, -40, 1, 38, 38, -38, 33, -35, -28, -40, 4,
        -15, -29, -33, -18, -9, -29, 20, 1, 36, -8, 23, -34, 16, -7, 13, 39, 38, 7, -7, -10, 30, 9, 26, 27, -37, -18,
        -25, 14, -36, 23, 28, -15, 35, -9, 1]
k = 8

print(maxSubsequence(nums, 8))
