# https://leetcode.com/problems/first-unique-character-in-a-string/description/
# https://www.youtube.com/watch?v=rBENYgWy3xU

def firstUniqChar(s):
    hashChar = {}
    for i in range(len(s)):
        c = s[i]
        if c not in hashChar:
            hashChar[c] = 1
        else:
            hashChar[c] += 1

    # if count == 1, it means it is unique
    # return the index of char immediately

    for i, char in enumerate(s):
        if hashChar[char] == 1:
            return i
    return -1


lst = "aabb"
print(firstUniqChar(lst))
