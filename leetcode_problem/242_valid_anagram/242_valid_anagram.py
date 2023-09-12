# https://leetcode.com/problems/valid-anagram/
# https://www.youtube.com/watch?v=9UtInBqnCgA&t=1s

def isAnagram(s, t):
    countS = {}
    countT = {}

    if len(s) != len(t):
        return False

    for i in range(len(s)):

        # count all character in string s
        if s[i] not in countS:
            countS[s[i]] = 1  # put that character into hashmap
        else:
            countS[s[i]] = 1 + countS[s[i]]  # update count

        # count all character in string t
        if t[i] not in countT:
            countT[t[i]] = 1
        else:
            countT[t[i]] = 1 + countT[t[i]]

    # compare 2 hashmap
    for c in countS:
        if (c not in countT) or (c not in countS) or (countS[c] != countT[c]):
            return False

    # must check all character in hashmap, if only 1 different ==> False
    return True


s_string = "rat"
t_string = "car"

print(isAnagram(s_string, t_string))
