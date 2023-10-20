# https://leetcode.com/problems/last-stone-weight/description/
# https://www.youtube.com/watch?v=B-QCq79-Vfw
import heapq


def lastStoneWeight(stones):
    # because we need maxHeap but python only has minHeap
    # => convert array to negative
    for i in range(len(stones)):
        stones[i] *= (-1)

    # transform list to heap
    heapq.heapify(stones)

    # we want to stop when array has 0 or 1 element
    while len(stones) > 1:
        # get the biggest stone
        first = heapq.heappop(stones)

        # get the second-biggest stone
        second = heapq.heappop(stones)

        if first != second:
            dif = first - second
            heapq.heappush(stones, dif)

    if len(stones) == 0:
        return 0
    else:
        return abs(stones[0])


stones = [1]
print(lastStoneWeight(stones))
