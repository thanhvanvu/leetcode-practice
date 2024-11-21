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

def characterReplacement_practice(s, k):
    L = 0
    longest = 0
    char_count = {}

    for R in range(len(s)):
        char = s[R]

        # count char and put in hash map
        if char not in char_count:
            char_count[char] = 1
        else:
            char_count[char] += 1

        # calculate window
        window = R - L + 1

        # get most frequency character in hashmap
        mostF = max(char_count.values())

        # check condition window - mostF = K
        # if not, keep shrinking the window until condition met
        while window - mostF > k:
            char_count[s[L]] -= 1
            L += 1

            # update window
            window = R - L + 1

            # update mostF
            mostF = max(char_count.values())

        longest = max(longest, window)

    return longest

s = "ABABBA"
k = 2

print(characterReplacement_practice(s, k))
