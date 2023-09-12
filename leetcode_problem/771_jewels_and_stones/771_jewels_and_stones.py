# https://leetcode.com/problems/jewels-and-stones/


def numJewelsInStones(jewels, stones):

    count = 0

    # loop through all character in stone and check if that char is in jewels
    # if yes, count += 1
    for char in stones:
        if char in jewels:
            count += 1

    return count


j = "aA"
s = "aAAbbbb"

print(numJewelsInStones(j, s))
