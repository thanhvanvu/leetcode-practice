def numOfSubarrays_bruteFroce(arr, k, threshold):
    count = 0
    L = 0

    for R in range(len(arr)):
        if R - L > k - 1:
            L += 1

        if R - L == k - 1:
            window = arr[L:R + 1]
            thres = sum(window) // k
            if thres >= threshold:
                count += 1

    return count


# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

def numOfSubarray(arr, k, threshold):
    count = 0
    L = 0
    R = k
    total = sum(arr[L:R])

    if total // k >= threshold:
        count += 1

    for R in range(k, len(arr)):
        if R - L > k - 1:
            total = total - arr[L]
            L += 1

        total += arr[R]
        thres = total // k

        if thres >= threshold:
            count += 1

    return count


def numOfSubarray_practice(arr, k, threshold):
    L = 0
    total = 0
    result = 0
    for R in range(len(arr)):
        num = arr[R]
        total = total + num

        if R - L + 1 == k:
            average = total // k
            if average >= threshold:
                result += 1

            # shrink window to find new subarray
            total = total - arr[L]
            L += 1
    return result


arr = [2, 2, 2, 2, 5, 5, 5, 8]
k = 3
threshold = 4

print(numOfSubarray_practice(arr, k, threshold))
