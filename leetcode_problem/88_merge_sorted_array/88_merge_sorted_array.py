def merge(nums1, m, nums2, n):
    last = m + n - 1

    while m > 0 and n > 0:
        if nums1[m - 1] > nums2[n - 1]:
            nums1[last] = nums1[m - 1]
            m -= 1
        else:
            nums1[last] = nums2[n - 1]
            n -= 1

        last -= 1

    while n > 0:
        nums1[last] = nums2[n - 1]
        n -= 1
        last -= 1
    return nums1


def merge_practice(nums1, m, nums2, n):
    i = m-1
    j = n - 1

    k = len(nums1) - 1

    # Merge in reverse order
    while i >= 0 and j >= 0:
        if nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1

    # If there are remaining elements in nums2, add them
    while j >= 0:
        nums1[k] = nums2[j]
        j -= 1
        k -= 1
    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [4, 5, 6]
n = 3

print(merge_practice(nums1, m, nums2, n))
