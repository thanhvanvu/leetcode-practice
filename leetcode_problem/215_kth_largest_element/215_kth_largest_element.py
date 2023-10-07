# https://www.youtube.com/watch?v=XEmy13g1Qxc
# https://leetcode.com/problems/kth-largest-element-in-an-array/


def findKthLargest(nums, k):
    # re-assign k
    k = len(nums) - k

    def quickSelect(arr, left, right):
        pivot = nums[right]
        p = left

        for i in range(left, right):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1

        # swap pivot to nums[p]
        nums[p], nums[right] = nums[right], nums[p]

        # p is now somewhere in the middle
        # [4, 2, 1, 3, 4, 6, 8, 9]
        # p = 4
        # k = 2
        # quickSelect from l to r
        if k < p:
            return quickSelect(arr, left, p - 1)

        # quickSelect from p + 1 to last element
        elif k > p:
            return quickSelect(arr, p + 1, right)

        elif k == p:
            return nums[p]

    return quickSelect(nums, 0, len(nums) - 1)


nums = [3,2,3,1,2,4,5,5,6]
k = 4

print(findKthLargest(nums, k))
