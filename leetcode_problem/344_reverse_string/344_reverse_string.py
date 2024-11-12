# https://leetcode.com/problems/reverse-string/description/

def reverseString(s):
    l = 0
    r = len(s) - 1

    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    return s


lst = ["h","e","l","l","o"]
print(reverseString(lst))
