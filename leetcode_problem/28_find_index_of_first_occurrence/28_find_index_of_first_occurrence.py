# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/description/

def strStr(haystack, needle):
    n = 0

    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        if needle[n] == haystack[i]:
            while i < len(haystack):
                if needle[n] == haystack[i]:
                    i += 1
                    n += 1
                    if n == len(needle):
                        return i - len(needle)
                else:
                    n = 0
                    break
        return -1



hay = "sadbutsad"
need = "sad"

print(strStr(hay, need))
