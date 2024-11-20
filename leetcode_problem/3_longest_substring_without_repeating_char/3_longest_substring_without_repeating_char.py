def lengthOfLongestSubstring(s):
    charSet = set()

    l = 0

    length = 0

    for r in range(len(s)):
        while s[r] in charSet:
            charSet.remove(s[l])
            l += 1

        # if char is not in charSet:
        charSet.add(s[r])

        sizeWindow = r - l + 1
        length = max(length, sizeWindow)

    return length


def lengthOfLongestSubstring_practice(s):
    # to check repeating character
    # use set()
    charSet = set()
    length = 0
    L = 0
    for R in range(len(s)):
        char = s[R]
        while s[R] in charSet:
            charSet.remove(s[L])
            L += 1

        # if char not in charset:
        charSet.add(s[R])

        sizeWindow = R - L + 1
        length = max(length, sizeWindow)

    return length


s = "abcabcbb"
print(lengthOfLongestSubstring_practice(s))
