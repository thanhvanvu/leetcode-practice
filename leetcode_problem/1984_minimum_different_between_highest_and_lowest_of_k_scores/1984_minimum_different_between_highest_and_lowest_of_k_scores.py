# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/description/
# https://www.youtube.com/watch?v=JU5XdBZZtlk

def minimumDifference(nums, k):
    nums.sort()

    # set up the window
    # k = 2 -> window = [0,1]
    # k = 3 -> window = [0,1,2]
    L = 0
    R = k - 1

    lowest = float("inf")

    while R < len(nums):
        diff = nums[R] - nums[L]
        lowest = min(lowest, diff)
        L += 1
        R += 1

    return lowest


lst = [9, 4, 1, 7]

# [1,4,7,9]
# [1,4] -> 4-1 = 3 => min = 3
# [4,7] -> 7-4 = 3 => min = 3
# [7,9] -> 9-7 = 2 => min = min(3,2) = 2

print(minimumDifference(lst, 2))
