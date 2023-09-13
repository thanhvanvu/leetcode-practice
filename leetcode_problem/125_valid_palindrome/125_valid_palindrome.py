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


string = "race a car"

print(isPalindrome(string))
