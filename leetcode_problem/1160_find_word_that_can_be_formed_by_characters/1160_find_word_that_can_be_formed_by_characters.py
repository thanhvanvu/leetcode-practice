# https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/description/
# https://www.youtube.com/watch?v=EQ5jTZdEn8Y


import copy
from collections import defaultdict


def countCharacters_test(words, chars: str) -> int:
    countChar = {}
    countTotal = 0

    for i in chars:
        if i not in countChar:
            countChar[i] = 1
        else:
            countChar[i] += 1

    for word in words:
        tempCountChar = copy.deepcopy(countChar)
        countWord = 0
        for c in word:
            if c not in tempCountChar or tempCountChar[c] == 0:
                break
            else:
                tempCountChar[c] -= 1
                countWord += 1
        if countWord == len(word):
            countTotal += len(word)

    return countTotal


def countCharacters(words, chars: str) -> int:
    countChar = {}
    countTotal = 0

    for i in chars:
        if i not in countChar:
            countChar[i] = 1
        else:
            countChar[i] += 1

    for word in words:
        cur_word = defaultdict(int)
        good = True

        for c in word:
            cur_word[c] += 1
            if c not in countChar or cur_word[c] > countChar[c]:
                good = False
                break

        if good:
            countTotal += len(word)

    return countTotal


words = ["hello", "world", "leetcode"]
chars = "welldonehoneyr"

print(countCharacters(words, chars))
