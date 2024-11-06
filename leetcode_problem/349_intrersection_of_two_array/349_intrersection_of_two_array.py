# https://leetcode.com/problems/intersection-of-two-arrays/description/


def intersection(nums1, nums2):
    num1_set = set(nums1)
    num2_set = set(nums2)
    output = []
    for i in num2_set:
        if i in num1_set:
            output.append(i)

    return output


nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersection(nums1, nums2))
