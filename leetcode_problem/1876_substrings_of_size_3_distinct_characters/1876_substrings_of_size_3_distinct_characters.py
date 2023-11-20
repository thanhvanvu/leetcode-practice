def countGoodSubstrings(s):
    charCount = {}
    L = 0
    result = 0
    for R in range(len(s)):
        while R - L + 1 > 3:
            cLeft = s[L]
            if charCount[cLeft] <= 1:
                del charCount[cLeft]
            else:
                charCount[cLeft] -= 1
            L += 1

        char = s[R]
        charCount[char] = 1 + charCount.get(char, 0)

        if len(charCount) == 3:
            result += 1

    return result

s = "aababcabc"
print(countGoodSubstrings(s))
