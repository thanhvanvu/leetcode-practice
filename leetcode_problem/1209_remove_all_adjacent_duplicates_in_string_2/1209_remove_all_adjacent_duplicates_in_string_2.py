# https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/description/
# https://www.youtube.com/watch?v=w6LcypDgC4w

def removeDuplicates(s: str, k: int):
    stack = []  # pair: [char, count]
    for c in s:

        if stack and c == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])

        # [ [a, 3], [b, 2], [f, 4] ]
        # 4 == 4
        # pop() --> pop([f, 4])
        if stack[-1][1] == k:
            stack.pop()

    result = ""

    # [a,3]
    # a*3 = aaa
    for char, count in stack:
        result += char * count

    return result


s = "deeedbbcccbdaa"
k = 3
print(removeDuplicates(s, k))
