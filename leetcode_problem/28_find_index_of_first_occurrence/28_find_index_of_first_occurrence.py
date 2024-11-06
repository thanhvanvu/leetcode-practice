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


def strStr1(haystack, needle):
    h = 0
    n = 0
    output = ""
    if len(haystack) < len(needle):
        return -1

    for i in range(len(haystack)):
        h = i

        while h < len(haystack) and n < len(needle):
            if haystack[h] == needle[n]:
                output += haystack[h]
                h += 1
                n += 1
            else:
                output = ""
                n = 0
                break

        if len(output) == len(needle):
            return i

    return -1

hay = "leetcode"
need = "leeto"

print(strStr1(hay, need))
