# https://leetcode.com/problems/get-equal-substrings-within-budget/description/
# https://www.youtube.com/watch?v=3lsT1Le526U
def equalSubstring(s: str, t: str, maxCost: int):
    L = 0
    max_output = 0
    total_cost = 0

    for R in range(len(s)):
        s_char = s[R]
        t_char = t[R]
        cost = abs(ord(s_char) - ord(t_char))
        total_cost += cost

        # shrinking the window
        if total_cost > maxCost:
            total_cost -= abs(ord(s[L]) - ord(t[L]))  # remove the most left element
            L += 1

        window = R - L + 1
        max_output = max(max_output, window)

    return max_output


s = "pxezla"
t = "loewbi"
maxCost = 25
print(equalSubstring(s, t, maxCost))
