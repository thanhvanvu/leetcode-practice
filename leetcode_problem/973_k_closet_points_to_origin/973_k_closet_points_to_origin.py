import heapq
import math


def kClosest(points, k):
    minHeap = []
    result = []

    # calculate distance
    # append result to minHeap [dis, x, y]
    for x, y in points:
        distance = math.sqrt((x ** 2) + (y ** 2))
        minHeap.append([distance, x, y])

    # transform list to heap
    heapq.heapify(minHeap)

    # pop min value from heap up to K
    # k = 2 => pop 2 min values
    # k = 4 => pop 4 min values
    while k > 0:
        dist, x, y = heapq.heappop(minHeap)

        result.append([x, y])
        k -= 1

    return result


points = [[3, 3], [5, -1], [-2, 4]]
print(kClosest(points, 2))
