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


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
