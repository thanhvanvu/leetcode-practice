# https://leetcode.com/problems/assign-cookies/description/
# https://www.youtube.com/watch?v=JW8fgvoxPTg

def findContentChildren(g, s):
    # sort both g, s ascending order
    g.sort()
    s.sort()

    i = j = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:
            i += 1
        j += 1

    return i


g = [1, 2, 3]

s = [1, 1, 3]

# sort ascending
# g = [1, 2, 3]
# s = [1, 1, 3]
# g[0] = s[0] = 1 => ok g1 need 1 cookie and s1 has 1 cookie -> satisfied
# g[1] = 2 > s[1] = 1 => not ok because g2 need 2 cookies but s1 has only 1 cookie -> not satisfied
# g[1]= 2 < s[2] = 3 => ok because g2 need 2 cookies and s3 has more cookies than g2 needs -> satisfied
# => only 2 students are satisfied

print(findContentChildren(g, s))
