# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

def arrayStringsAreEqual(word1, word2):
    str1 = ""
    str2 = ""
    for word in word1:
        str1 += word

    for word in word2:
        str2 += word

    return True if str1 == str2 else False


word1 = ["ab", "c"]
word2 = ["a", "bc"]
print(arrayStringsAreEqual(word1, word2))
