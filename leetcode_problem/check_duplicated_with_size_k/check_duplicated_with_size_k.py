def closeDuplicates(nums, k):
    window = set()
    L = 0

    for R in range(len(nums)):
        # window size > k
        # k = 3
        # window size = 4
        # increase L
        # window size = 3
        # remove the most left element in the set
        if R - L + 1 > k:
            L += 1
            window.remove(nums[L])

        # found duplicate in size k
        if nums[R] in window:
            return True

        # if the element is not in set()
        window.add(nums[R])

    # after the loop is end
    # meaning no duplicated
    return False



input = [1,2,3,1]
k = 3

print(closeDuplicates(input, k))
