# https://leetcode.com/problems/find-first-palindromic-string-in-the-array/description/
# https://www.youtube.com/watch?v=4JA5MW772N0

def firstPalindrome(words):
    for str in words:
        l = 0
        r = len(str) - 1

        # set a flag
        # special technical
        is_palindromic = True
        while l < r:
            if str[l] == str[r]:
                l += 1
                r -= 1
            else:
                is_palindromic = False
                break

        if is_palindromic is True:
            return str

    return ""


# cheating way
# to check if it is palindrome, just reverse it
# car # rac -> not
# racecar = racecar -> palindrome

def firstPalindrome_cheating(words):
    for str in words:
        str_reverse = str[::-1]  # need to google
        if str == str_reverse:
            return str

    # for loop is done -> cant find palindrome string
    # return ""
    return ""


words = ["abc", "car", "ada", "racecar", "cool"]

print(firstPalindrome_cheating(words))
