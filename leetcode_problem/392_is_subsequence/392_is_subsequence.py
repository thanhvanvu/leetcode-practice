def isSubsequence(s: str, t: str) -> bool:
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


s = ""
t = "ahbgdc"

print(isSubsequence(s, t))
