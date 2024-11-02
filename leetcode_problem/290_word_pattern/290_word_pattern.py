# https://leetcode.com/problems/word-pattern/submissions/1440526398/
# https://leetcode.com/problems/isomorphic-strings/description/
# https://www.youtube.com/watch?v=W_akoecmCbM

def wordPattern(pattern: str, s: str) -> bool:
    s = s.split(' ')

    # if 2 length of string not equal -> false
    if len(pattern) != len(s):
        return False

    # map every char in pattern to s
    # map every string in s to pattern
    charToWord = {}
    wordToChar = {}
    for i in range(len(pattern)):
        char, word = pattern[i], s[i]

        # a -> dog (good)
        # a -> fish
        # a is in hashmap, but hash[a] = fish != dog -> False
        if (char in charToWord and charToWord[char] != word) or (word in wordToChar and wordToChar[word] != char):
            return False

        charToWord[char] = word
        wordToChar[word] = char

    return True


ptt = "abba"
txt = "dog cat cat dog"
print(wordPattern(ptt, txt))
