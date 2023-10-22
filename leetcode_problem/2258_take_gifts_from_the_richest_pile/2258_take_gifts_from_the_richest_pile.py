# https://leetcode.com/problems/take-gifts-from-the-richest-pile/description/

import heapq
import math


def pickGifts(gifts, k):
    # make array to be negative
    gifts = [-i for i in gifts]
    heapq.heapify(gifts)

    while k > 0:

        # get maximum
        maximum = heapq.heappop(gifts)

        # calculate value
        # because maximum = -5
        # convert it to 5 and take sqrt
        value = math.sqrt(abs(maximum))

        # convert it to negative and push back to heap
        heapq.heappush(gifts, math.ceil(value*-1))

        k -= 1

    total = 0

    # calculate total of every element
    for i in gifts:
        total += abs(i)

    return int(total)


gifts = [25, 64, 9, 4, 100]
k = 4

print(pickGifts(gifts, 4))