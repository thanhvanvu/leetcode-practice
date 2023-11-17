def characterReplacement(s, k):
    L = 0
    result = 0
    sCount = {}

    for R in range(len(s)):
        char = s[R]

        if char not in sCount:
            sCount[char] = 1
        else:
            sCount[char] += 1

        # make sure current window is valid
        windowSize = R - L + 1

        # get the maximum value from hashSet
        mostF = max(sCount.values())

        while windowSize - mostF > k:
            sCount[s[L]] -= 1
            L += 1

            # update windowSize and the most frequently character
            windowSize = R - L + 1
            mostF = max(sCount.values())

        result = max(result, windowSize)

    return result


s = "ABABBA"
k = 2

print(characterReplacement(s, k))
