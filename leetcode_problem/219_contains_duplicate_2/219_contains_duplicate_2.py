def containsNearbyDuplicate(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        # case window is too big
        if R - L > k:
            window.remove(nums[L])
            L += 1

        if nums[R] in window:
            return True

        # if nums[R] is not in window
        # add to set
        window.add(nums[R])

    return False

nums = [1, 2, 3, 1]
k = 3
print(containsNearbyDuplicate(nums, k))