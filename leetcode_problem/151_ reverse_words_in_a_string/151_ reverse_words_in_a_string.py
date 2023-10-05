def reverseWords(s):
    s = s.strip().split()
    string = ''
    l = 0
    r = len(s) - 1

    print(s)
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1

    for i in range(len(s)):
        if i == len(s)-1:
            string += s[i]
        else:
            string = string + s[i] + ' '

    return string


s = "a    good   example"
print(reverseWords(s))
