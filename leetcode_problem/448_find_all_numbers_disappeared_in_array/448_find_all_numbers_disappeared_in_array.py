# https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/

def findDisappearedNumbers(nums):
    # [0, 0, 0, 0, 0, 0, 0, 0, 0]
    temp = [0] * (len(nums) + 1)

    result = []

    # [0, 1, 1, 1, 1, 0, 0, 1, 1]
    for i in nums:
        temp[i] = 1

    # find index that = 0 => return index
    k = 1
    while k < len(temp):
        if temp[k] == 0:
            result.append(k)
        k += 1

    return result


lst = [4, 3, 2, 7, 8, 2, 3, 1]
print(findDisappearedNumbers(lst))
