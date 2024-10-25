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


def isAnagram2(s, t):
    # count every character and store in hashmap
    countS = {}
    countT = {}

    # if 2 strings have different length -> return False
    if len(s) != len(t):
        return False

    # count all char in s
    for char in range(len(s)):
        if s[char] not in countS:
            countS[s[char]] = 1
        else:
            countS[s[char]] += 1

    # count all char in t
    for char in range(len(t)):
        if t[char] not in countT:
            countT[t[char]] = 1
        else:
            countT[t[char]] += 1

    # compare 2 hashmap
    # countS = {'r': 1, 'a': 1}
    # countT = {'c': 1, 'a': 1}
    # r is not in count T -> return false
    for c in countS:
        if (c not in countT) or (c not in countS) or (countS[c] != countT[c]):
            return False

    return True


s_string = "rat"
t_string = "tar"
print(isAnagram2(s_string, t_string))
