# https://leetcode.com/problems/valid-palindrome-ii/description/
# https://www.youtube.com/watch?v=JrxRYBwG6EI

def validPalindrome(s):
    L = 0
    R = len(s) - 1

    while L < R:
        if s[L] == s[R]:
            L += 1
            R -= 1
        else:
            # L = 0, R = 3
            # "abcd", to get "abc" -> s[L : R] = s[0 : 3], python will run 0,1,2
            left_string = s[L: R]
            left_reversed = left_string[::-1]

            # L = 0, R = 3
            # "abcd", to get "bcd" -> s[L+1 : R+1] = s[1 : 4], python will run 1,2,3
            right_string = s[L + 1: R+1]
            right_reversed = right_string[::-1]

            if left_string == left_reversed or right_string == right_reversed:
                return True
            else:
                return False

    return True


string = "abc"

# s = "cbbcc"
# c = c -> good
# b # c -> do not know what to remove, so try both side
# 1/ remove left char -> "bc" -> reverse("bc") = cd -> cd # bc
# 2/ remove right char -> "bb" -> reverse("bb") = bb -> bb = bb
# from 2 conditions, we should remove left character
# check if reverse string == original string, if yes -> palindrome else no palindrome
print(validPalindrome(string))
