# https://leetcode.com/problems/ransom-note/description/?envType=study-plan-v2&envId=top-interview-150

def canConstruct(ransomNote: str, magazine: str) -> bool:

    hashMagazin = {}
    for i in magazine:
        if i not in hashMagazin:
            hashMagazin[i] = 1
        else:
            hashMagazin[i] += 1

    for j in ransomNote:
        if j in hashMagazin:
            hashMagazin[j] -= 1

            if hashMagazin[j] == 0:
                hashMagazin.pop(j)
        else:
            return False

    return True


ransomNote = "aa"
magazine = "aabb"

print(canConstruct(ransomNote, magazine))
