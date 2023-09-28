# O(n*m)
# https://leetcode.com/problems/keyboard-row/description/

def findWords(words):
    key = {
        "z": 1,
        "x": 1,
        "c": 1,
        "v": 1,
        "b": 1,
        "n": 1,
        "m": 1,
        "a": 2,
        "s": 2,
        "d": 2,
        "f": 2,
        "g": 2,
        "h": 2,
        "j": 2,
        "k": 2,
        "l": 2,
        "q": 3, "w": 3, "e": 3, "r": 3, "t": 3, "y": 3, "u": 3, "i": 3, "o": 3, "p": 3
    }

    i = 0

    # loop through the array
    while i < len(words):
        word = words[i]
        k = key[word[0].lower()]
        for char in words[i]:
            # check every char has the same value of key
            # if not, remove that word from the list
            # reset i = 0
            if key[char.lower()] != k:
                words.remove(word)
                i = -1
                break
        i += 1
    return words


words = ["abdfs","cccd","a","qwwewm"]
print(findWords(words))
