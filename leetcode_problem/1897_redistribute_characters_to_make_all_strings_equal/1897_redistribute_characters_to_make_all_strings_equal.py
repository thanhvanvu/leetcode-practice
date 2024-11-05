# https://leetcode.com/problems/redistribute-characters-to-make-all-strings-equal/description/
# https://www.youtube.com/watch?v=a3SmUiimBi8

def makeEqual(words):
    countChar = {}
    length = len(words)

    for word in words:
        for c in word:
            if c not in countChar:
                countChar[c] = 1
            else:
                countChar[c] += 1

    # count % len(words), if == 0, we can make all string equal, example 6%3=0 -> [aa, aa, aa] good
    # if > 0, we can not --> example 5 % 3 = 2 --> [aa, aa, a] not good
    for char in countChar:
        if countChar[char] % length != 0:
            return False

    return True


# words = ["abc","aabc","bc"]
# understand easily, just count every character
# count % len(words), if == 0, we can make all string equal, example 6%3=0 -> [aa, aa, aa] good
# if > 0, we can not --> example 5 % 3 = 2 --> [aa, aa, a] not good
words = ["ab", "a"]
print(makeEqual(words))
