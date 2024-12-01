# https://leetcode.com/problems/arranging-coins/description/
# https://www.youtube.com/watch?v=5rHz_6s2Buw

# brute force
def arrangeCoins(n):
    i = 0

    while True:
        i += 1
        n = n - i

        if n < 0:
            return i - 1
        elif n == 0:
            return i


def arrangeCoins_binary(n):
    # n is coins

    L = 0
    R = n
    res = 0

    while L <= R:
        row = L + (R - L) // 2

        # coin need to complete r row = (r/2) * (r + 1)
        coin_need = (row / 2) * (row + 1)

        if coin_need > n:
            R = row - 1
        else:
            # row could be 1, 2
            # it means, with 5 coins, we can complete 1 row, 2 row
            # we want to return the biggest row
            L = row + 1
            res = max(row, res)

    return res

n = 5

# * -> 5 - 1 = 4
# ** -> 4 - 2 = 2
# *** -> 2 - 3 = -1
# n < 0 -> return i - 1 = 2
# n = 0 -> return i


# this formula only works when start from 1 -> n
# 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
# total = 55
# formular = (r/2) * (r + 1) = (10/2) * (10+1) = 55
# example:
# r = 5 -> (5/2) * (5+1) = 15, it means we need at least 15 coins to complete 5 rows
# r = 3 -> (3/2) * (3+1) = 6, it means we need at least 6 coins to complete 3 rows
print(arrangeCoins_binary(n))
