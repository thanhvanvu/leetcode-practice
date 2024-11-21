# https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
# https://www.youtube.com/watch?v=vgBrQ0NM5vE

def maxFrequency(nums, k):
    nums.sort()
    max_f = 0
    L = 0
    total = 0
    for R in range(len(nums)):
        total += nums[R]
        window = R - L + 1

        # Check if the current window is valid
        if nums[R] * window - total > k:
            total -= nums[L]  # Remove the leftmost number from the total
            L += 1  # shrink window

        # Update the maximum frequency
        max_f = max(max_f, R - L + 1)

    return max_f


# to calculate the most freq
# nums[R] * current size window - total
# [1] -> 1 * 1 - 1 = 0
# [1, 2] -> total = 3 -> 2 * 2 - 3 = 1
# [1, 2, 4] -> total = 7 -> 4 * 3 - 7 = 5
# [1, 2, 4, 6] -> total = 13 -> 6 * 4 = 11 ===> shrink window
# to shrink window -> total - 1 = 12, L+= 1
nums = [1, 4, 8, 13]
k = 5
print(maxFrequency(nums, k))
