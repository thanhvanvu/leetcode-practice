# https://leetcode.com/problems/minimum-number-of-flips-to-make-the-binary-string-alternating/description/
# https://www.youtube.com/watch?v=MOeuK6gaC2A

def minFlips(s: str):
    length = len(s)
    alt0 = ""
    alt1 = ""

    diff0 = 0
    diff1 = 0

    # double length of s
    # s = 01001
    # newS = 0100 + 0100 = 01000100
    s = s + s

    # create alternating string with length of s
    # 01010101
    # 10101010
    for i in range(len(s)):
        if i % 2 == 0:
            alt0 += "0"
            alt1 += "1"
        else:
            alt0 += "1"
            alt1 += "0"

    # sliding window
    l = 0
    res = len(s)

    for r in range(len(s)):
        num = s[r]
        if num != alt0[r]:
            diff0 += 1

        if num != alt1[r]:
            diff1 += 1

        window = r - l + 1

        # shrink window
        # remove the most left element
        # check if the most left element is different
        # decrease 1
        # length is the initial length before s = s + s
        if window > length:
            if s[l] != alt0[l]:
                diff0 -= 1

            if s[l] != alt1[l]:
                diff1 -= 1
            l += 1

        if r - l + 1 == length:
            res = min(res, diff0, diff1)

    return res


s = "01001001101"
print(minFlips(s))
