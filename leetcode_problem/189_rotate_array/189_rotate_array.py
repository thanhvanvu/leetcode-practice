# https://leetcode.com/problems/rotate-array/description/
# https://www.youtube.com/watch?v=BHr381Guz3Y

def rotate(nums, k):
    # k could be more than length of nums
    # [1,2], k = 3
    # k = 3%2 = 1
    k = k % len(nums)

    # reverse it
    nums.reverse()

    # reverse first half
    L = 0
    R = k - 1
    while L < R:
        nums[L], nums[R] = nums[R], nums[L]
        L += 1
        R -= 1

    # reverse second half
    left = k
    right = len(nums) - 1
    while left < right:
        nums[left], nums[right] = nums[right], nums[left]
        left += 1
        right -= 1

    return nums


nums = [-1, -100, 3, 99]
k = 2
print(rotate(nums, k))
