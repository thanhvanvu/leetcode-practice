# https://www.youtube.com/watch?v=sqWOFIZ9Z0U&t=388s
# https://leetcode.com/problems/monotonic-array/description/

def isMonotonicMySolotion(nums):
    i = 1

    # [1] ==> true
    if len(nums) == 1:
        return True

    while i < len(nums):
        # [1,1,1,2,3]
        # if left == right ==> i + 1
        if nums[i] == nums[i - 1]:
            i += 1

            # case [1,1,1]
            if i == len(nums):
                return True
        else:
            # increase
            if nums[i] > nums[i - 1]:
                r = i
                while r < len(nums) - 1:
                    # if left > right ==> decrease ==> False
                    if nums[r] > nums[r + 1]:
                        return False
                    r += 1
                return True

            # decrease
            if nums[i] < nums[i - 1]:
                r = i
                while r < len(nums) - 1:
                    # if left < right ==> increase ==> false
                    if nums[r] < nums[r + 1]:
                        return False
                    r += 1
                return True


def isMonotonic(nums):
    increase = True  # Assume it's increasing by default
    decrease = True  # Assume it's decreasing by default

    for i in range(len(nums) - 1):
        # [1,2,3,0,4] ==> increase = False at 0
        if not nums[i] <= nums[i + 1]:
            increase = False

        # [6,5,3,2,9,4] ==> decrease = False at 9
        if not nums[i] >= nums[i + 1]:
            decrease = False

    # true or true ==> true
    # true or false ==> false
    # false or false ==> false
    return increase or decrease


def isMonotonic_practice(nums):
    increase = True
    decrease = True

    for i in range(len(nums) - 1):
        if not (nums[i] <= nums[i + 1]):
            increase = False

        if not (nums[i] >= nums[i + 1]):
            decrease = False

    # true or true ==> true
    # true or false ==> false
    # false or false ==> false
    return increase or decrease


nums = [6, 5, 4, 4]

print(isMonotonic_practice(nums))
