def isSubsequence1(s: str, t: str) -> bool:
    i = 0  # pointer for t
    j = 0  # pointer for s

    while i < len(t) and j < len(s):
        if t[i] == s[j]:
            j += 1
        i += 1

    if j == len(s):
        return True
    else:
        return False


def isSubsequence(s: str, t: str):
    # use 2 pointer to check every character from 2 sting
    i, j = 0, 0

    # base case
    if len(s) == 0 or len(t) == 0:
        return False

    for j in range(len(t)):
        if s[i] == t[j]:
            i += 1
        if i == len(s):
            return True

    return False


s = "axc"
t = "ahbgdc"

print(isSubsequence(s, t))
