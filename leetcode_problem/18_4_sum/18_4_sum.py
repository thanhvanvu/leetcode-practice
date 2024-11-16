def fourSum(nums, target):
    nums.sort()
    is_exist = set()
    result = []
    L = 0
    R = len(nums) - 1

    while L < R:
        two_sum = nums[L] + nums[R]

        left = L + 1
        right = R - 1

        while left < right:
            four_sum = nums[left] + nums[right] + two_sum
            if four_sum < target:
                left += 1
            elif four_sum > target:
                right -= 1
            else:
                if (nums[L], nums[left], nums[right], nums[R]) not in is_exist:
                    is_exist.add((nums[L], nums[left], nums[right], nums[R]))
                    result.append([nums[L], nums[left], nums[right], nums[R]])

                left += 1
                right -= 1

        if two_sum > target:
            R -= 1
        elif two_sum < target:
            L += 1
        else:
            R -= 1
            L += 1

    return result


nums = [2, 2, 2, 2, 2]
target = 8
print(fourSum(nums, target))
