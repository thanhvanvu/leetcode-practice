# https://www.youtube.com/watch?v=sadDk3AsFEw
# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

def numberOfSubstrings_bruteForce(s: str) -> int:
    countSet = set()
    result = 0
    for L in range(len(s)):
        for R in range(L, len(s)):
            char = s[R]
            countSet.add(char)

            if len(countSet) == 3:
                result += 1
        countSet.clear()
    return result


def numberOfSubstrings(s):
    count = {'a': 0, 'b': 0, 'c': 0}
    result = 0
    L = 0

    for R in range(len(s)):
        char = s[R]
        count[char] = 1 + count.get(char, 0)

        # abcabc
        # 012345
        # L = 0
        # R = 2
        # abc => good
        # the # of substring can be made with abc
        # len(s) - R = 6 -2 = 4
        # abc, abca, abcab, abcabc
        while count['a'] >= 1 and count['b'] >= 1 and count['c'] >= 1:
            result += len(s) - R
            count[s[L]] -= 1
            L += 1

    return result


s = "abc"
print(numberOfSubstrings(s))
