# https://leetcode.com/problems/find-the-difference-of-two-arrays/description/


def findDifference(nums1, nums2):
    num1_set = set(nums1)
    num2_set = set(nums2)
    output = []

    result1 = []
    result2 = []
    for num in num1_set:
        if num not in num2_set:
            result1.append(num)
    output.append(result1)

    for num in num2_set:
        if num not in num1_set:
            result2.append(num)
    output.append(result2)


    return output


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(findDifference(nums1, nums2))
