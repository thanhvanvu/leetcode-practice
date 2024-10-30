# https://leetcode.com/problems/isomorphic-strings/description/
# https://www.youtube.com/watch?v=7yF-U1hLEqQ

def isIsomorphic(s, t):
    # 2 string will always have the same length
    # Map char in S to char in T
    # Map char in T to char in S

    mapST, mapTS = {}, {}

    for i in range(len(s)):
        char1, char2 = s[i], t[i]

        # check if character is in hashmap or not first
        # if char1, char2 are not in hashmap yet -> insert it to hashmap
        if (char1 in mapST and mapST[char1] != char2) or (char2 in mapTS and mapTS[char2] != char1):
            return False

        mapST[char1] = char2
        mapTS[char2] = char1

    return True


a = "foo"
b = "bar"
print(isIsomorphic(a, b))
