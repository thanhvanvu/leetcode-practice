# https://leetcode.com/problems/guess-number-higher-or-lower/description/

def guessNumber(n):
    l = 1
    r = n

    while l <= r:
        m = (l + r) // 2

        if isCorrect(m) == 1:
            r = m - 1
        elif isCorrect(m) == -1:
            l = m + 1
        else:
            return m


def isCorrect(n):
    if n > 1:
        return 1
    elif n < 1:
        return -1
    else:
        return 0


num = 1
pick = 1

print(guessNumber(num))
