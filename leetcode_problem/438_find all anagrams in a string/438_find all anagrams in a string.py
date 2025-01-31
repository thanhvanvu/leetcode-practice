# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
# https://www.youtube.com/watch?v=G8xtZy0fDKg&ab_channel=NeetCode

def findAnagrams(s, p):
    sCount = {}
    pCount = {}

    result = []

    if len(s) < len(p):
        return result

    for i in range(len(p)):
        numS = s[i]
        numP = p[i]

        if numP not in pCount:
            pCount[numP] = 1
        else:
            pCount[numP] += 1

        if numS not in sCount:
            sCount[numS] = 1
        else:
            sCount[numS] += 1

    print(sCount)
    print(pCount)

    if sCount == pCount:
        result.append(0)

    l = 0
    for r in range(len(p), len(s)):
        print(s[l], s[r])

        if s[r] not in sCount:
            sCount[s[r]] = 1
        else:
            sCount[s[r]] += 1

        # before increase l
        # remove character at position l in sCount
        sCount[s[l]] -= 1

        # if sCount[x] == 0, pop it out hashmap
        if sCount[s[l]] == 0:
            sCount.pop(s[l])

        l += 1

        if sCount == pCount:
            result.append(l)

    return result


s = "abab"
p = "ab"

print(findAnagrams(s, p))
