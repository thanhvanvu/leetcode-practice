# https://leetcode.com/problems/permutation-in-string/description/

# count char in s1 and put in hashmap s1_count
# loop through s2
# check the window, window is a length of s1
# if we see char in s2 that in s1
# count it and put in hashmap s2_count
# compare hashmap s1_count == s2_count ==> true

def checkInclusion(s1, s2):
    n1, n2 = len(s1), len(s2)

    # edge case
    if n1 > n2:
        return False

    s1_count = {}
    s2_count = {}
    L = 0

    for c in s1:
        s1_count[c] = s1_count.get(c, 0) + 1

    for R in range(len(s2)):

        if R - L + 1 > len(s1):
            if s2[L] in s2_count:
                s2_count[s2[L]] -= 1
            L += 1

        char = s2[R]
        if char in s1_count:
            s2_count[char] = s2_count.get(char, 0) + 1

        if s1_count == s2_count:
            return True

    return False


def checkInclusion_practice(s1, s2):
    n1, n2 = len(s1), len(s2)

    # edge case
    if n1 > n2:
        return False

    s1Count = {}
    s2Count = {}

    # count char s1
    for char in s1:
        if char not in s1Count:
            s1Count[char] = 1
        else:
            s1Count[char] += 1

    L = 0

    for R in range(len(s2)):
        # only put char that is in s1count
        char = s2[R]
        if char in s1Count:
            if char not in s2Count:
                s2Count[char] = 1
            else:
                s2Count[char] += 1

        window = R - L + 1

        # check when window size > len(s1)
        # shrinking window until condition met
        if window > len(s1):
            # pop the most left element in s2
            if s2[L] in s2Count:
                s2Count[s2[L]] -= 1
            L += 1

        # check if 2 hashcounts equal
        # yes -> permutation
        if s1Count == s2Count:
            return True

    # for loop done -> cant find permutation
    return False


# check permutation
# count s1
# count s2
# compare s1 == s2 --> return True
# check window, if window > len(s1)
# shrink window, remove most left character in count hashmap
s1 = "ab"
s2 = "eidbaooo"
print(checkInclusion_practice(s1, s2))
