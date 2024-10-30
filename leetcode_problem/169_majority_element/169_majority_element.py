# https://leetcode.com/problems/majority-element/description/
# https://www.youtube.com/watch?v=7yF-U1hLEqQ
import math


def majorityElement(nums):
    freq = math.floor(len(nums) / 2)

    hashCount = {}

    # count how many element appears
    # store in hash map
    # {1: 3, 2: 4}
    for i in nums:
        if i not in hashCount:
            hashCount[i] = 1
        else:
            hashCount[i] += 1

    # check which element appears more than ⌊n / 2⌋ times
    for num in hashCount:
        if hashCount[num] > freq:
            return num


# O(1) space complexity
# nums = [2,2,1,1,1,2,2]
# count = 0
# result = 1
# for i in nums
# i = 2 ----> count = 1, result = 2
# i = 2 = result ----> count = 1 + 1 = 2, result = 2
# i = 1 # result ----> count = 2 - 1 = 1, result = 2
# i = 1 # result ----> count = 1 - 1 = 1, result = 2
# i = 1 # result ----> count = 1 - 1 = 0, result will be assigned to new value = 1, count = 1
# i = 2 # result ----> count = 1 - 1 = 0, result will be assigned to new value = 2, count = 1
# i = 2 = result ----> count = 1 + 1 = 2, result 2
# finish, return result = 2

def majority(nums):
    count = 0
    result = 0

    for i in nums:
        if count <= 0:
            count = 1
            result = i
        elif result == i:
            count += 1
        else:
            count -= 1
    return result


lst = [3,3,4]
print(majority(lst))
