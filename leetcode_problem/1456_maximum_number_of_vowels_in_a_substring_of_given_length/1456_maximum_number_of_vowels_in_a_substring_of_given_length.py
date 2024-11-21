# https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/
# https://www.youtube.com/watch?v=kEfPSzgL-Ss

def maxVowels(s: str, k: int) -> int:
    vowel = {"a", "e", "i", "o", "u"}
    maximum = 0
    count = 0

    L = 0

    for R in range(len(s)):

        # calculate window
        window = R - L + 1

        # if window > k
        # shrink window until condition meets
        # if the most left element is not in vowel
        # decrease count
        if window > k:
            if s[L] in vowel:
                count -= 1
            L += 1

        char = s[R]

        # if element in vowel
        # count +1
        if char in vowel:
            count += 1

        # calculate maximum
        maximum = max(maximum, count)

        # if we see count == window
        # just return it immediately
        if count == k:
            return count

    return maximum


s = "zpuerktejfp"
k = 3
print(maxVowels(s, k))
