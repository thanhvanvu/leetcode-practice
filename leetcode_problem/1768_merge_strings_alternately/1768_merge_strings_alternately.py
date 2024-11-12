# https://leetcode.com/problems/merge-strings-alternately/description/
# https://www.youtube.com/watch?v=JU5XdBZZtlk

def mergeAlternately(word1, word2):
    left = 0
    result = []

    while left < len(word1) and left < len(word2):
        result.append(word1[left])
        result.append(word2[left])
        left += 1

    # after while, it will have case length of 2 string are not equal

    # if len(word1) < len(word2)
    result.append(word2[left:])

    # if len(word2) < len(word1)
    result.append(word1[left:])

    return "".join(result)


word1 = "ab"
word2 = "pqrs"
print(mergeAlternately(word1, word2))
