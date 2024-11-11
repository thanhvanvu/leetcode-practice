# https://www.youtube.com/watch?v=jJXJ16kPFWg
# https://leetcode.com/problems/valid-palindrome/description/

def isPalindrome(s: str):
    # use 2 pointers
    left = 0
    right = len(s) - 1  # len(s) = 5 ==> right = 4

    # 2 pointers will shift to middle and break while loop
    while left < right:

        # check if character is a special char => shift pointer
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True


def isPalindrome_practice(s):
    L = 0
    R = len(s) - 1

    while L < R:
        if s[L].lower() == s[R].lower():
            L += 1
            R -= 1

        elif not s[L].isalnum():  # if s[L] is not alphabet
            L += 1

        elif not s[R].isalnum():
            R -= 1
        else:  # if s[L] != s[R]
            return False

    return True


string = "A man, a plan, a canal: Panama"

print(isPalindrome_practice(string))
