# https://leetcode.com/problems/largest-substring-between-two-equal-characters/description/
# https://www.youtube.com/watch?v=66b2V_rCuJw

def maxLengthBetweenEqualCharacters(s):
    indexChar = {}
    largestLength = -1

    for i in range(len(s)):
        c = s[i]

        if c not in indexChar:
            indexChar[c] = i
        else:
            length = i - indexChar[c] - 1
            largestLength = max(largestLength, length)

    return largestLength


# s = "abca"
# we can see "a" index 0, another "a" index 3
# to calculate length substring, 3 - 0 - 1 = 2
# what if s = "abcarea" ?
# we have 3 "a" at index 0, 3, 6
# we want to use the furthest "a" - first "a"
# how to remember the index of first "a" ? --> use hashmap to store the index
# -> one loop solution
# go through every char
# if char "a" not in hashMap -> store the index
# if we see that char "a" again, calculate the length

s = "aa"
print(maxLengthBetweenEqualCharacters(s))
