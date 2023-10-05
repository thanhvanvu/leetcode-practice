# https://leetcode.com/problems/reverse-string-ii/description/

def reverseStr(s, k):
    s = list(s)
    i = 0
    l = 0
    r = k - 1

    # case: "abcd", k = 2
    # len = 4 < 2 ==> reverse all string
    if len(s) < k:
        l = 0
        r = len(s) - 1
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    # loop through string
    while i < len(s):

        # check if l pointer is in range
        # yes => swap
        while l < r and l < len(s):
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

        i = i + 2 * k  # shift pointer to the next 2K
        l = i  # assign l = i
        r = l + k - 1  # assign r

        # check if r is out of bound
        # set r = the last item
        if r >= len(s):
            r = len(s) - 1

    return "".join(s)


s = "abcdefg"
k = 2
print(reverseStr(s, k))
