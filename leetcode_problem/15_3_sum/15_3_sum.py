# https://www.youtube.com/watch?v=jzZsG8n2R9A
# https://leetcode.com/problems/3sum/description/

def threeSum(nums):
    nums.sort()

    result_three_some = []

    for i in range(len(nums)):

        # [1, 1, 2, 3, 6...]
        # i will be shift = 2
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        l = i + 1
        r = len(nums) - 1

        # [1, 1, 2, 3, 6, 8...]
        # 2 + 2sum[3, 6, 8] = 0 => return
        while l < r:
            two_sum = nums[l] + nums[r]
            if two_sum > -nums[i]:
                r -= 1
            elif two_sum < -nums[i]:
                l += 1
            else:
                result_three_some.append([nums[i], nums[l], nums[r]])
                l += 1

                while nums[l] == nums[l-1] and l < r:
                    l += 1

    return result_three_some


# def twoSum(list, target):
#     target = - target
#     result = []
#     l = 0
#     r = len(list) - 1
#     while l < r:
#         two_sum = list[l] + list[r]
#
#         if two_sum < target:
#             l += 1
#         elif two_sum > target:
#             r -= 1
#         else:
#             array = [target, list[l], list[r]]
#             result.append(array)
#             l += 1
#
#     return result


list_num = [-1, 0, 1, 2, -1, -4]
# print(threeSum(list_num))
threeSum(list_num)
