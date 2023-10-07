# big(O) = n^2
def sortArray_insertion(nums):
    # loop through an array from second element
    for i in range(1, len(nums)):
        j = i - 1
        while j >= 0 and nums[j + 1] < nums[j]:
            nums[j + 1], nums[j] = nums[j], nums[j + 1]
            j -= 1

    return nums


# https://www.youtube.com/watch?v=MsYZSinhuFo
def sortArray_merge(nums):
    def merge(arr, L, M, R):

        # clone the arrays
        left = arr[L: M + 1]
        right = arr[M + 1: R + 1]

        k = L
        i = 0
        j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1

            k += 1

        # case if left arr still has number
        while i < len(left):
            nums[k] = left[i]
            k += 1
            i += 1

        # case if right arr still has number
        while j < len(right):
            nums[k] = right[j]
            k += 1
            j += 1

        return arr

    def mergeSort(arr, left, right):
        # size arr = 1 [0]
        if left == right:
            return arr

        # calculate mid point
        mid = (left + right) // 2

        # recursive

        # first half
        mergeSort(arr, left, mid)

        # second half
        mergeSort(arr, mid + 1, right)

        # once it gets to base case, start merging
        merge(arr, left, mid, right)

        return arr

    return mergeSort(nums, 0, len(nums) - 1)


def sortArray_quickSort(nums):
    def quickSort(arr, s, e):
        # last - first + 1 = length
        if e - s + 1 <= 1:
            return arr

        # pick pivot = the last element
        pivot = arr[e]
        left = s

        for i in range(s, e):
            if arr[i] < pivot:
                arr[left], arr[i] = arr[i], arr[left]
                left += 1

        # Move pivot in-between left and right sides
        arr[left], arr[e] = arr[e], arr[left]

        # quick sort left side
        quickSort(arr, s, left - 1)

        # quick sort right side
        quickSort(arr, left + 1, e)

        return arr

    return quickSort(nums, 0, len(nums) - 1)


n = [5, 2, 3, 1, 8, 4, 4, 0, 6]
print(sortArray_quickSort(n))
