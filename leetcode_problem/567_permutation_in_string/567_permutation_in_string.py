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


s1 = "ab"
s2 = "eidboaoo"
print(checkInclusion(s1, s2))
