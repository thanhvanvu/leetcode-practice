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


def containsNearbyDuplicate_practice(nums, k):
    L = 0

    # numSet to check duplicate
    window = set()

    for R in range(len(nums)):
        # window must be <= k
        # window = R - L = 4 - 0 = 4 > k
        # remove the most left element from nums in window
        # change window
        if R - L > k:
            window.remove(nums[L])
            L += 1

        # found duplicate
        if nums[R] in window:
            return True

        # if element is not in set() -> add it to set
        window.add(nums[R])

    # for loop is done -> no duplicate
    return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
print(containsNearbyDuplicate_practice(nums, k))
