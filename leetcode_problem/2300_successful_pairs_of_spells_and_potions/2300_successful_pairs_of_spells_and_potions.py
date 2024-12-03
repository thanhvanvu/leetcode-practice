# https://leetcode.com/problems/successful-pairs-of-spells-and-potions/description/
# https://www.youtube.com/watch?v=OKnm5oyAhWg

def successfulPairs_bruteForce(spells, potions, success):
    result = []
    for s in spells:
        count = 0
        for p in potions:
            product = s * p
            if product >= success:
                count += 1
        result.append(count)
    return result


def successfulPairs(spells, potions, success):
    result = []
    potions.sort()
    length_potions = len(potions)
    for s in spells:
        L = 0
        R = len(potions) - 1
        max_pair = 0
        while L <= R:
            mid = L + (R - L) // 2
            product = s * potions[mid]
            if product < success:
                L = mid + 1
            else:
                size = length_potions - mid
                max_pair = max(max_pair, size)
                R = mid - 1

        result.append(max_pair)
    return result


spells = [5, 1, 3]
potions = [1, 2, 3, 4, 5]
success = 7

# idea is find the smallest potions that spell * potion >= success
# [1,2,3,4,5]
# we find 3 (3,4,5 are good) but it may not be smallest, so we check left side
# we find 2 (2,3,4,5 are good)
# everytime we find the good potions, calculate max good pair and append to result
print(successfulPairs(spells, potions, success))
