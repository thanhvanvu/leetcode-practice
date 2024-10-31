# https://leetcode.com/problems/maximum-number-of-balloons/description/
# https://www.youtube.com/watch?v=G9xeB2-7PqY
import math


def maxNumberOfBalloons(text):
    example = "balloon"
    balloon = {}
    hashCount = {}
    result = float("inf")

    # count how many char required to make "balloon"
    # {'b': 1, 'a': 1, 'l': 2, 'o': 2, 'n': 1}
    for t in example:
        if t not in balloon:
            balloon[t] = 1
        else:
            balloon[t] += 1

    # count how many character
    for t in text:
        if t in balloon:
            if t not in hashCount:
                hashCount[t] = 1
            else:
                hashCount[t] += 1

    # to make string balloon, 2 hashMap must be same length
    # if not same length, return 0
    if len(balloon) != len(hashCount):
        return 0

    # calculate the ratio
    # l:4 --> 4/2 = 2 --> we can make 2 strings "balloon"
    # l:2 --> 2/2 = 1 --> we can make 1 string "balloon
    # o:3 --> 3/2 = 1 --> we can make 1 string "balloon
    # how many strings we can make = min ratio value
    for c in hashCount:
        ratio = math.floor(hashCount[c] / balloon[c])
        result = min(result, ratio)

    return result


txt = "balon"
print(maxNumberOfBalloons(txt))
