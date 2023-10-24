# https://www.youtube.com/watch?v=0d6WF79hQME

import bisect


def kthSmallest(matrix, k):
    l = matrix[0][0]
    r = matrix[-1][-1]
    N = len(matrix)

    def less_k(m):
        count = 0
        for row in range(N):
            x = bisect.bisect_right(matrix[row], m)
            count += x
        return count

    while l < r:
        mid = (l + r) // 2
        if less_k(mid) < k:
            l = mid + 1
        else:
            r = mid
    return l


matrix = [[1, 5, 9], [10, 11, 13], [12, 13, 15]]
k = 8

print(kthSmallest(matrix, k))
