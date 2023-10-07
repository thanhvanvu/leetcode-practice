import math


# https://leetcode.com/problems/koko-eating-bananas/description/
# https://www.youtube.com/watch?v=U2SozAs9RzA

def minEatingSpeed(piles, h):
    # rate is from 1 - max(piles)
    l = 1
    r = max(piles)
    min_rate = r  # set min = maximum

    while l <= r:
        mid = (l + r) // 2

        total_time = 0

        # calculate the total hour koko takes to eat all bananas
        for p in piles:
            total_time = total_time + math.ceil(p / mid)


        # if total time < h
        # need to check more if any k that makes total time < h
        if total_time <= h:
            min_rate = min(min_rate, mid)
            r = mid - 1

        # if total time > h
        # increase rate range (second half) to search
        if total_time > h:
            l = mid + 1

    return min_rate


piles = [3, 6, 7, 11]
h = 8

print(minEatingSpeed(piles, h))
