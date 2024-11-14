def twoSum(numbers, target):
    # create 2 pointers
    l = 0
    r = len(numbers) - 1

    # [2, 7, 11, 15], 9

    while l < r:
        # l = 2, r = 15
        # sum = 2 + 15 = 19 > 9
        # r -= 1 ==> r = 11

        # sum = 2 + 11 = 13 > 9
        # r -= 1 ==> r = 7

        # sum = 2 + 7 = 9
        # ==> return

        sum = numbers[l] + numbers[r]
        if sum < target:
            l += 1
        elif sum > target:
            r -= 1
        else:
            return [l + 1, r + 1]


# array must be sorted
# use 2 pointer technique
def twoSum_practice(numbers, target):
    L = 0
    R = len(numbers) - 1

    while L < R:
        L_num = numbers[L]
        R_num = numbers[R]
        total = L_num + R_num

        if total == target:
            return [L + 1, R + 1]

        if total < target:
            L += 1
        else:
            R -= 1


nums = [2, 3, 4]
value = 6

print(twoSum_practice(nums, value))
