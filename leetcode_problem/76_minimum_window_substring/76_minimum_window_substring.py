# https://www.youtube.com/watch?v=jSto0O4AJbM
# https://leetcode.com/problems/minimum-window-substring/
def minWindow(s, t):
    tCount = {}
    window = {}
    L = 0
    minimum = float('inf')
    result = ""

    # count char and put into hashmap tCount
    for i in t:
        if i not in tCount:
            tCount[i] = 1
        else:
            tCount[i] += 1

    have = 0
    need = len(tCount)

    for R in range(len(s)):
        char = s[R]

        if char not in window:
            window[char] = 1
        else:
            window[char] += 1

        if char in tCount and window[char] == tCount[char]:
            # update "have"
            have += 1

        while have == need:
            length = R - L + 1
            if length < minimum:
                result = s[L:R]
                minimum = length

            c = s[L]
            window[c] -= 1
            if c in tCount and window[c] < tCount[c]:
                # update have
                have -= 1

            L += 1

    return result


s = "cabwefgewcwaefgcf"
t = "cae"

print(minWindow(s, t))
