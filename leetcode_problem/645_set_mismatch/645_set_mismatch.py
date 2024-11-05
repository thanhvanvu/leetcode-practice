# https://leetcode.com/problems/set-mismatch/description/
# https://www.youtube.com/watch?v=d-ulaeRBA64
from collections import defaultdict


def findErrorNums(nums):
    numbers_hash = defaultdict(int)
    x = y = 0
    # count number and store in hashmap:
    for number in nums:
        numbers_hash[number] += 1

    # loop through [1,N],
    for i in range(1, len(nums) + 1):  # [1,2,2,4] 1->4
        # if value > 1 --> duplicate
        if numbers_hash[i] > 1:
            x = i

        # if value = 0 -> missing number
        if numbers_hash[i] == 0:
            y = i

    return [x, y]


lst = [1, 1]
print(findErrorNums(lst))
