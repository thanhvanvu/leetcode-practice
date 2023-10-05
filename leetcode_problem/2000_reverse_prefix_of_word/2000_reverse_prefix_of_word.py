# https://leetcode.com/problems/reverse-prefix-of-word/description/
# O(n)

def reversePrefix(word, ch):
    word = list(word)  # convert string to array
    l = 0
    r = 0
    i = 0

    # loop through the array
    while i < len(word):

        # check if element == ch
        # set r pointer = i
        if word[i] == ch:
            r = i

            # swap 2 character
            while l < r:
                word[l], word[r] = word[r], word[l]
                l += 1
                r -= 1
            return "".join(word)
        else:
            # if not found element == ch
            # increase pointer
            i += 1
    return "".join(word)


word = "abcd"
ch = "z"

print(reversePrefix(word, ch))